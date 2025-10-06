# precios/models/precio_analisis.py
from django.db import models
from analisis.models import Analisis

class PrecioAnalisis(models.Model):
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE, related_name='precios')
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    moneda = models.CharField(max_length=10, default='PEN')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.analisis.nombre} - {self.monto} {self.moneda}"

