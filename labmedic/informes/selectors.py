from .models import Informe

def informes_por_paciente(nombre):
    return Informe.objects.filter(registro_examen__paciente__icontains=nombre)
