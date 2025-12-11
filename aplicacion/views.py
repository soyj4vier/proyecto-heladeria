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
from aplicacion.forms import ClienteForm, MovimientoPuntosForm, ProductoForm, PromocionForm
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
        impacto_economico=F('usos') * F('valor_descuento')  # Calcular el impacto
    ).order_by('-usos')

    return render(request, 'aplicacion/dashboard_promociones.html', {
        'promociones': promociones,
    })

def buscar_clientes(request):
    query = request.GET.get('q', '')
    print(f"Término de búsqueda recibido: {query}")

    clientes = Cliente.objects.filter(
        nombre__icontains=query
    ) | Cliente.objects.filter(
        run__icontains=query
    ) 

    print(f"Clientes encontrados: {clientes}")

    
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

    print(f"Datos enviados al frontend: {clientes_data}") 
    return JsonResponse({'clientes': clientes_data})

def buscar_promociones(request):
    query = request.GET.get('q', '')  
    promociones = Promocion.objects.filter(
        nombre__icontains=query
    ) | Promocion.objects.filter(
        descripcion__icontains=query
    )  

    
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
                cliente.puntos = 0  # Evita que los puntos sean negativos
            cliente.save()

            
            movimiento.save()
            return redirect('inicio')
    else:
        form = MovimientoPuntosForm()
    return render(request, 'aplicacion/movimientoadd.html', {'form': form})

@login_required
def crear_promocion(request):
    if request.method == 'POST':
        formulario = request.POST.get('formulario')

        if formulario == 'registrar_producto':
            producto_form = ProductoForm(request.POST)
            if producto_form.is_valid():
                producto_form.save()
                return render(request, 'aplicacion/promocionesadd.html', {
                    'mensaje_producto': 'Producto registrado correctamente.',
                    'producto_form': ProductoForm(),
                    'promocion_form': PromocionForm(),
                })
            else:
                return render(request, 'aplicacion/promocionesadd.html', {
                    'producto_form': producto_form,
                    'promocion_form': PromocionForm(),
                })

        elif formulario == 'registrar_promocion':
            promocion_form = PromocionForm(request.POST)
            if promocion_form.is_valid():
                promocion_form.save()
                return render(request, 'aplicacion/promocionesadd.html', {
                    'mensaje_promocion': 'Promoción registrada correctamente.',
                    'producto_form': ProductoForm(),
                    'promocion_form': PromocionForm(),
                })
            else:
                return render(request, 'aplicacion/promocionesadd.html', {
                    'producto_form': ProductoForm(),
                    'promocion_form': promocion_form,
                })

    return render(request, 'aplicacion/promocionesadd.html', {
        'producto_form': ProductoForm(),
        'promocion_form': PromocionForm(),
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
    print(f"Run recibido para modificar: {run}")
    cliente = get_object_or_404(Cliente, run=run)
    print(f"Cliente encontrado: {cliente}")

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            print("Cliente modificado exitosamente.")
            return redirect('inicio')
        else:
            print(f"Errores en el formulario: {form.errors}")
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
    promocion = get_object_or_404(Promocion, id=promocion_id)

    total_descuento = promocion.valor_descuento * promocion.usos
    impacto_economico = total_descuento 

    context = {
        'promocion': promocion,
        'usuario': request.user,
        'usos': promocion.usos,
        'total_descuento': total_descuento,
        'impacto_economico': impacto_economico,
    }

    # Renderizar el HTML del reporte
    template_path = 'aplicacion/reporte_promocion.html'
    html = render_to_string(template_path, context)

    # Crear el archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_promocion_{promocion.id}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Verificar si hubo errores al generar el PDF
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el reporte.', status=500)

    return response

@login_required
def sistema_transaccional(request):
    if request.method == 'POST':
        formulario = request.POST.get('formulario')
        print(f"Formulario enviado: {formulario}")

        if formulario == 'registrar_transaccion':
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
                cliente.puntos = 0  # Evita puntos negativos
            cliente.save()

            return render(request, 'aplicacion/transaccion.html', {
                'mensaje': 'Puntos actualizados correctamente.',
                'clientes': Cliente.objects.all(),
                'promociones': Promocion.objects.filter(activo=True),
                'productos': Producto.objects.all(),
            })

    return render(request, 'aplicacion/transaccion.html', {
        'clientes': Cliente.objects.all(),
        'promociones': Promocion.objects.filter(activo=True),
        'productos': Producto.objects.all(),
    })