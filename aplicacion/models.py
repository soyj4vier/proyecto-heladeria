from django.db import models

# Create your models here.

class Cliente(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='RUN')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    puntos = models.IntegerField(default=0, verbose_name='Puntos')

    def __str__(self):
        return "El cliente {} tiene {} puntos".format(self.nombre, self.puntos)
    
    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

class MovimientoPuntos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='movimientos')
    fecha = models.DateTimeField(auto_now_add=True)
    puntos = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"El cliente {self.cliente.nombre} Tiene {self.puntos} a la fecha de {self.fecha}"
    
    class Meta:
        managed = False
        db_table = 'movimiento_puntos'
        verbose_name = 'Movimiento puntos'
        verbose_name_plural = 'Movimientos Puntos'
