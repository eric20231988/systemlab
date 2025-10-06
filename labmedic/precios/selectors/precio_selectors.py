from ..models import PrecioAnalisis

def obtener_precios_vigentes():
    return PrecioAnalisis.objects.filter(fecha_fin__isnull=True).select_related('analisis')

def obtener_precios_por_analisis(analisis_id):
    return PrecioAnalisis.objects.filter(analisis_id=analisis_id).order_by('-fecha_inicio')
