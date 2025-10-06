from django.db import models
from registrar_examenes.models import RegistroExamen

class Informe(models.Model):
    registro_examen = models.OneToOneField(RegistroExamen, on_delete=models.CASCADE)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Informe de {self.registro_examen.paciente} - {self.fecha_generacion.date()}"
