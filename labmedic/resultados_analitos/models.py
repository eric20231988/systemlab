from django.db import models
from registrar_examenes.models import RegistroExamen
from analitos.models import Analito

class ResultadoAnalito(models.Model):
    registro_examen = models.ForeignKey(RegistroExamen, on_delete=models.CASCADE)
    analito = models.ForeignKey(Analito, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[
        ('normal', 'Normal'),
        ('alto', 'Alto'),
        ('bajo', 'Bajo'),
        ('pendiente', 'Pendiente')
    ], default='pendiente')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.registro_examen.paciente} - {self.analito.nombre}"
