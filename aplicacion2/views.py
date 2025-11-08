from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def datos(request):
    data = {
        'nombre': ' Javier',
        'apellido': 'Pérez',
        'edad': 20,
        'sexo': 'Masculino'
    }
    return render(request, 'aplicacion2/datos.html', data)

def index(request):
    return render(request, 'aplicacion2/index.html')