from django.contrib import admin
from aplicacion2.models import Promocion, Producto

# Register your models here.
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_descuento', 'activo', 'fecha_inicio', 'fecha_fin', 'usos')
    list_filter = ('activo', 'tipo_descuento')
    search_fields = ('nombre', 'descripcion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio']

admin.site.register(Promocion, PromocionAdmin)
admin.site.register(Producto, ProductoAdmin)
