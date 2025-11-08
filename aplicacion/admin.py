from django.contrib import admin
from aplicacion.models import Cliente, MovimientoPuntos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['run', 'nombre', 'apellido_paterno', 'apellido_materno', 'puntos']

class MovimientoPuntosAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'puntos', 'descripcion', 'fecha']

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(MovimientoPuntos, MovimientoPuntosAdmin)
