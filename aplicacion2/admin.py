from django.contrib import admin
from aplicacion2.models import TipoDescuento, Promocion, DetallePromocion, Producto, ProductoPromocion

# Register your models here.
class PromocionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_inicio', 'fecha_fin', 'activo']

class TipoDescuentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']

class DetallePromocionAdmin(admin.ModelAdmin):
    list_display = ['promocion', 'tipo_descuento', 'valor_descuento', 'codigo_promocional']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio']

class ProductoPromocionAdmin(admin.ModelAdmin):
    list_display = ['producto', 'promocion']

admin.site.register(TipoDescuento, TipoDescuentoAdmin)
admin.site.register(Promocion, PromocionAdmin)
admin.site.register(DetallePromocion, DetallePromocionAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoPromocion, ProductoPromocionAdmin)
