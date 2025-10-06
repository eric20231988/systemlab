from ..models import Analisis

def obtener_analisis():
    return Analisis.objects.all()
