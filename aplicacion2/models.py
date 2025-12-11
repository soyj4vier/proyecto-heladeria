from django.db import models

# Create your models here.

class Promocion(models.Model):
    TIPO_DESCUENTO_CHOICES = [
        ('porcentual', 'Porcentual'),
        ('dinero', 'Resta en dinero'),
    ]

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)
    usos = models.IntegerField(default=0)
    tipo_descuento = models.CharField(max_length=10, choices=TIPO_DESCUENTO_CHOICES, default='porcentual')
    codigo_promocional = models.CharField(max_length=20, blank=True, null=True)
    valor_descuento = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_descuento}) - Activo: {self.activo}"
    
    class Meta:
        db_table = 'promocion'
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'


class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"El producto ingresado es {self.nombre} y el precio es {self.precio}"
    
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
