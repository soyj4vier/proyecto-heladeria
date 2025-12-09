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
from aplicacion.models import Cliente, MovimientoPuntos
from aplicacion2.models import Producto, Promocion
import datetime

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
            movimiento = form.save(commit=False)
            cliente = movimiento.cliente

            # Actualizar los puntos del cliente
            cliente.puntos += movimiento.puntos
            if cliente.puntos < 0:
                cliente.puntos = 0  # Evitar que los puntos sean negativos
            cliente.save()

            # Guardar el movimiento
            movimiento.save()
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
        detalle_form = DetallePromocionForm(request.POST, prefix='detalle')  # Agregar el formulario de detalle

        if producto_form.is_valid() and promocion_form.is_valid() and tipo_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save()
            promocion = promocion_form.save(commit=False)
            promocion.save()
            tipo_descuento = tipo_form.save()
            detalle_promocion = detalle_form.save(commit=False)
            detalle_promocion.promocion = promocion  # Vincular el detalle con la promoción creada
            detalle_promocion.save()
            return redirect('inicio')
        else:
            # Depuración: Imprimir errores en la consola
            print("Errores en ProductoForm:", producto_form.errors)
            print("Errores en PromocionForm:", promocion_form.errors)
            print("Errores en TipoDescuentoForm:", tipo_form.errors)
            print("Errores en DetallePromocionForm:", detalle_form.errors)

            return render(request, 'aplicacion/promocionesadd.html', {
                'producto_form': producto_form,
                'promocion_form': promocion_form,
                'tipo_form': tipo_form,
                'detalle_form': detalle_form,  # Pasar el formulario de detalle al contexto
            })
    else:
        producto_form = ProductoForm(prefix='producto')
        promocion_form = PromocionForm(prefix='promocion')
        tipo_form = TipoDescuentoForm(prefix='tipo')
        detalle_form = DetallePromocionForm(prefix='detalle')  # Crear el formulario de detalle

    return render(request, 'aplicacion/promocionesadd.html', {
        'producto_form': producto_form,
        'promocion_form': promocion_form,
        'tipo_form': tipo_form,
        'detalle_form': detalle_form,  # Pasar el formulario de detalle al contexto
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

@login_required
def generar_reporte_promocion(request, promocion_id):
    # Obtener la promoción
    promocion = Promocion.objects.annotate(
        total_descuento=Sum('detallepromocion__valor_descuento'),
        impacto_economico=F('usos') * F('detallepromocion__valor_descuento')
    ).get(id=promocion_id)

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

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
    with open(ruta_archivo, 'rb') as archivo_pdf:
        response.write(archivo_pdf.read())
    return response

@login_required
def sistema_transaccional(request):
    if request.method == 'POST':
        formulario = request.POST.get('formulario')  # Identificar el formulario enviado
        print(f"Formulario enviado: {formulario}")

        if formulario == 'registrar_transaccion':
            # Procesar el formulario de registrar transacción
            cliente_run = request.POST.get('cliente')
            promocion_id = request.POST.get('promocion')
            producto_id = request.POST.get('producto')

            print(f"Cliente RUN recibido: {cliente_run}")
            print(f"Promoción ID recibida: {promocion_id}")
            print(f"Producto ID recibido: {producto_id}")

            if not cliente_run or not promocion_id or not producto_id:
                print("Error: Faltan datos en el formulario de transacción.")
                return render(request, 'aplicacion/transaccion.html', {
                    'mensaje': 'Error: Todos los campos son obligatorios.',
                    'clientes': Cliente.objects.all(),
                    'promociones': Promocion.objects.filter(activo=True),
                    'productos': Producto.objects.all(),
                })

            cliente = get_object_or_404(Cliente, run=cliente_run)
            promocion = get_object_or_404(Promocion, id=promocion_id)
            producto = get_object_or_404(Producto, id=producto_id)

            puntos_a_sumar = 10
            if promocion.activo:
                puntos_a_sumar += 5

            cliente.puntos += puntos_a_sumar
            cliente.save()

            promocion.usos += 1
            promocion.save()

            MovimientoPuntos.objects.create(
                cliente=cliente,
                puntos=puntos_a_sumar,
                descripcion=f"Transacción con promoción '{promocion.nombre}' y producto '{producto.nombre}'"
            )

            return render(request, 'aplicacion/transaccion.html', {
                'mensaje': 'Transacción procesada correctamente.',
                'clientes': Cliente.objects.all(),
                'promociones': Promocion.objects.filter(activo=True),
                'productos': Producto.objects.all(),
            })

        elif formulario == 'actualizar_puntos':
            # Procesar el formulario de actualizar puntos
            cliente_run = request.POST.get('cliente_puntos')
            puntos = request.POST.get('puntos')

            print(f"Cliente RUN recibido para actualizar puntos: {cliente_run}")
            print(f"Puntos recibidos: {puntos}")

            if not cliente_run or not puntos:
                print("Error: Faltan datos en el formulario de actualización de puntos.")
                return render(request, 'aplicacion/transaccion.html', {
                    'mensaje': 'Error: Todos los campos son obligatorios.',
                    'clientes': Cliente.objects.all(),
                    'promociones': Promocion.objects.filter(activo=True),
                    'productos': Producto.objects.all(),
                })

            cliente = get_object_or_404(Cliente, run=cliente_run)
            puntos = int(puntos)

            cliente.puntos += puntos
            if cliente.puntos < 0:
                cliente.puntos = 0  # Evitar puntos negativos
            cliente.save()

            return render(request, 'aplicacion/transaccion.html', {
                'mensaje': 'Puntos actualizados correctamente.',
                'clientes': Cliente.objects.all(),
                'promociones': Promocion.objects.filter(activo=True),
                'productos': Producto.objects.all(),
            })

    # Si es una solicitud GET, renderiza la página con los datos necesarios
    return render(request, 'aplicacion/transaccion.html', {
        'clientes': Cliente.objects.all(),
        'promociones': Promocion.objects.filter(activo=True),
        'productos': Producto.objects.all(),
    })