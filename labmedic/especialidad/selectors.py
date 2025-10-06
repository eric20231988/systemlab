from .models import Especialidad

def especialidades_activas():
    return Especialidad.objects.filter(activa=True)
