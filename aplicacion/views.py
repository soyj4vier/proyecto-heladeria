from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from aplicacion.forms import ClienteForm, MovimientoPuntosForm, ProductoForm, PromocionForm, TipoDescuentoForm, DetallePromocionForm, ProductoPromocionForm
from aplicacion2.models import Promocion
from aplicacion.models import Cliente

def index(request):
    return render(request, 'aplicacion/index.html')

def login_view(request):
    return render(request, 'registration/login.html')

def inicio(request):
    return render(request, 'aplicacion/inicio.html')

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


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'aplicacion/clientes.html', {'clientes': clientes})

def cargar_cliente(request, run):
    cliente = get_object_or_404(Cliente, run=run)
    form = ClienteForm(instance=cliente)

    return render(request, 'aplicacion/modificarcliente.html', {'form': form, 'cliente': cliente})

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

def eliminar_cliente(request, run):
    cliente = get_object_or_404(Cliente, run=run)
    cliente.delete()
    return redirect('listarclientes')

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