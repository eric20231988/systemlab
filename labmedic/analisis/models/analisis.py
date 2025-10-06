from django.db import models

class Analisis(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    unidad = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre
