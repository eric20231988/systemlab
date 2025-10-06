from django.db import models
from analisis.models import Analisis

class Analito(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20)
    valor_minimo = models.DecimalField(max_digits=6, decimal_places=2)
    valor_maximo = models.DecimalField(max_digits=6, decimal_places=2)
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE, related_name='analitos')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.unidad})"
