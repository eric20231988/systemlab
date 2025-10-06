from django.db import models
from analisis.models import Analisis
from precios.models import PrecioAnalisis
from .categoria import CategoriaExamen

class Examen(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaExamen, on_delete=models.CASCADE)
    analisis = models.ManyToManyField(Analisis, related_name='examenes')

    def __str__(self):
        return self.nombre

    def calcular_total(self):
        precios = PrecioAnalisis.objects.filter(analisis__in=self.analisis.all(), fecha_fin__isnull=True)
        subtotal = sum(p.monto for p in precios)
        igv = subtotal * 0.18
        return round(subtotal + igv, 2)
