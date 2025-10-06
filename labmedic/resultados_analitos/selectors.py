from .models import ResultadoAnalito

def resultados_pendientes():
    return ResultadoAnalito.objects.filter(estado='pendiente')

def resultados_completos():
    return ResultadoAnalito.objects.exclude(estado='pendiente')
