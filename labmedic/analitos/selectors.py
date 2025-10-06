from .models import Analito

def obtener_analitos_activos():
    return Analito.objects.filter(activo=True).select_related('analisis')
