from django.db import models

# Create your models here.

class TipoDescuento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tipo_promocion'
        verbose_name = 'Tipo Promocion'
        verbose_name_plural = 'Tipo de promociones'

class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)
    usos = models.IntegerField(default=0)

    def __str__(self):
        return f"La promoción {self.nombre} esta {self.activo}, fecha inicio: {self.fecha_inicio} fecha_fin: {self.fecha_fin}"
    
    class Meta:
        db_table = 'promocion'
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'

class DetallePromocion(models.Model):
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    tipo_descuento = models.ForeignKey(TipoDescuento, on_delete=models.CASCADE)
    valor_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_promocional = models.CharField(max_length=20, blank=True, null=True)
    condicion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.promocion} - {self.codigo_promocional}"
    
    class Meta:
        db_table = 'detalle_promocion'
        verbose_name = 'Detalle promocion'
        verbose_name_plural = 'Detalle promociones'

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"El producto ingresado es {self.nombre} y el precio es {self.precio}"
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class ProductoPromocion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto_promocion'
        verbose_name = 'Producto en promoción'
        verbose_name_plural = 'Productos en promoción'