from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    TIPO_DOC_CHOICES = [
        ('DNI', 'DNI'),
        ('CE', 'Carné de Extranjería'),
        ('PAS', 'Pasaporte'),
    ]
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOC_CHOICES, default='DNI')
    dni = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    creado_en = models.DateTimeField(default=timezone.now, editable=False)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creado_en']
        indexes = [
            models.Index(fields=['dni']),
            models.Index(fields=['apellidos', 'nombres']),
        ]
        permissions = [
            ('ver_pacientes', 'Puede ver pacientes'),
        ]

    def __str__(self):
        return f'{self.apellidos}, {self.nombres} ({self.dni})'
