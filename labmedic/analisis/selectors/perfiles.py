from ..models import PerfilAnalisis

def obtener_perfiles():
    return PerfilAnalisis.objects.prefetch_related('analisis').all()
