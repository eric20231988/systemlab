from .models import RegistroExamen

def examenes_por_estado(estado):
    return RegistroExamen.objects.filter(estado=estado).select_related('tipo_examen')
