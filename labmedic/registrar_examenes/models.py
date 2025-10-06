from django.db import models
from examen.models import TipoExamen
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroExamen(models.Model):
    paciente = models.CharField(max_length=150)
    tipo_examen = models.ForeignKey(TipoExamen, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado')
    ], default='pendiente')
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.paciente} - {self.tipo_examen.nombre}"
