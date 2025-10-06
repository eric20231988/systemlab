from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_documento', 'dni', 'apellidos', 'nombres', 'telefono', 'creado_en')
    search_fields = ('dni', 'apellidos', 'nombres', 'telefono', 'email')
    list_filter = ('tipo_documento', 'sexo')
    ordering = ('-creado_en',)
