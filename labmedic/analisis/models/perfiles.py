from django.db import models
from .analisis import Analisis

class PerfilAnalisis(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    analisis = models.ManyToManyField(Analisis, related_name='perfiles')

    def __str__(self):
        return self.nombre
