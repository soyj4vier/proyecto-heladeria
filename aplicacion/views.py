from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum, F
from django.template.loader import render_to_string
import os
from aplicacion.models import ReportePromocion
from django.conf import settings
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from aplicacion.forms import ClienteForm, MovimientoPuntosForm, ProductoForm, PromocionForm, TipoDescuentoForm, DetallePromocionForm, ProductoPromocionForm
from aplicacion2.models import Promocion
from aplicacion.models import Cliente

def index(request):
    return render(request, 'aplicacion/index.html')

def login_view(request):
    return render(request, 'registration/login.html')

@login_required
def inicio(request):
    return render(request, 'aplicacion/inicio.html')

@login_required
def dashboard_promociones(request):
    # Obtener las promociones con sus métricas
    promociones = Promocion.objects.annotate(
        total_descuento=Sum('detallepromocion__valor_descuento'),  # Total de descuentos aplicados
        impacto_economico=F('usos') * F('detallepromocion__valor_descuento')  # Impacto económico
    ).order_by('-usos')  # Ordenar por cantidad de usos

    return render(request, 'aplicacion/dashboard_promociones.html', {
        'promociones': promociones,
    })


def buscar_clientes(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    clientes = Cliente.objects.filter(
        nombre__icontains=query
    ) | Cliente.objects.filter(
        run__icontains=query
    )  # Filtrar por nombre o RUN

    # Serializar los resultados
    clientes_data = [
        {
            'run': cliente.run,
            'nombre': cliente.nombre,
            'apellido_paterno': cliente.apellido_paterno,
            'apellido_materno': cliente.apellido_materno,
            'puntos': cliente.puntos,
        }
        for cliente in clientes
    ]

    return JsonResponse({'clientes': clientes_data})

def buscar_promociones(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    promociones = Promocion.objects.filter(
        nombre__icontains=query
    ) | Promocion.objects.filter(
        descripcion__icontains=query
    )  # Filtrar por nombre o descripción

    # Serializar los resultados
    promociones_data = [
        {
            'id': promo.id,
            'nombre': promo.nombre,
            'descripcion': promo.descripcion,
            'fecha_inicio': promo.fecha_inicio.strftime('%Y-%m-%d'),
            'fecha_fin': promo.fecha_fin.strftime('%Y-%m-%d'),
            'activo': promo.activo,
        }
        for promo in promociones
    ]

    return JsonResponse({'promociones': promociones_data})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'aplicacion/clienteadd.html', {'form': form})

def crear_movimiento(request):
    if request.method == 'POST':
        form = MovimientoPuntosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MovimientoPuntosForm()
    return render(request, 'aplicacion/movimientoadd.html', {'form': form})

@login_required 
def crear_promocion(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, prefix='producto')
        promocion_form = PromocionForm(request.POST, prefix='promocion')
        tipo_form = TipoDescuentoForm(request.POST, prefix='tipo')

        if producto_form.is_valid() and promocion_form.is_valid() and tipo_form.is_valid():
            producto_form.save()
            promocion_form.save()
            tipo_form.save()
            return redirect('inicio')
    else:
        producto_form = ProductoForm(prefix='producto')
        promocion_form = PromocionForm(prefix='promocion')
        tipo_form = TipoDescuentoForm(prefix='tipo')

    return render(request, 'aplicacion/promocionesadd.html', {
        'producto_form': producto_form,
        'promocion_form': promocion_form,
        'tipo_form': tipo_form,
    })

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'aplicacion/clientes.html', {'clientes': clientes})

def cargar_cliente(request, run):
    cliente = get_object_or_404(Cliente, run=run)
    form = ClienteForm(instance=cliente)

    return render(request, 'aplicacion/modificarcliente.html', {'form': form, 'cliente': cliente})

@login_required
def modificar_cliente(request, run):
    cliente = get_object_or_404(Cliente, run=run)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'aplicacion/modificarcliente.html', {'form': form, 'cliente': cliente})

@login_required
def eliminar_cliente(request, run):
    cliente = get_object_or_404(Cliente, run=run)
    cliente.delete()
    return redirect('listarclientes')

@login_required
def listar_promociones(request):
    promociones = Promocion.objects.all()
    return render(request, 'aplicacion/promociones.html', {'promociones': promociones})

def cargar_promocion(request, id):
    promocion = get_object_or_404(Promocion, id=id)
    form = PromocionForm(instance=promocion)

    return render(request, 'aplicacion/modificarpromociones.html', {'form': form, 'promocion': promocion})

def modificar_promocion(request, id):
    promocion = get_object_or_404(Promocion, id=id)
    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PromocionForm(instance=promocion)
    
    return render(request, 'aplicacion/modificarpromociones.html', {'form': form, 'promocion': promocion})

def eliminar_promocion(request, id):
    promocion = get_object_or_404(Promocion, id=id)
    promocion.delete()
    return redirect('listarpromociones')

def saludo(request):
    return HttpResponse("Hola tú")

@login_required
def generar_reporte_promocion(request, promocion_id):
    # Obtener la promoción
    promocion = Promocion.objects.annotate(
        total_descuento=Sum('detallepromocion__valor_descuento'),
        impacto_economico=F('usos') * F('detallepromocion__valor_descuento')
    ).get(id=promocion_id)

    # Renderizar el contenido HTML para el PDF
    template_path = 'aplicacion/reporte_promocion.html'
    context = {
        'promocion': promocion,
        'usuario': request.user,
        'usos': promocion.usos,
        'total_descuento': promocion.total_descuento or 0,
        'impacto_economico': promocion.impacto_economico or 0,
    }
    html = render_to_string(template_path, context)

    # Crear el archivo PDF
    nombre_archivo = f"reporte_promocion_{promocion.id}_{request.user.username}.pdf"
    ruta_pdf = os.path.join(settings.STATICFILES_DIRS[0], 'pdf')
    if not os.path.exists(ruta_pdf):
        os.makedirs(ruta_pdf)
    ruta_archivo = os.path.join(ruta_pdf, nombre_archivo)

    with open(ruta_archivo, 'wb') as archivo_pdf:
        pisa_status = pisa.CreatePDF(html, dest=archivo_pdf)

    # Verificar si hubo errores
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el reporte.', status=500)

    # Guardar el reporte en la base de datos
    ReportePromocion.objects.create(
        usuario=request.user,
        nombre_archivo=nombre_archivo,
        promocion=promocion
    )

    # Descargar el archivo
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
    with open(ruta_archivo, 'rb') as archivo_pdf:
        response.write(archivo_pdf.read())

    return response