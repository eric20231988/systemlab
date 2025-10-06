from resultados_analitos.models import ResultadoAnalito
from registrar_examenes.models import RegistroExamen

def resultados_completos():
    return ResultadoAnalito.objects.filter(completo=True)

def examenes_pendientes():
    return RegistroExamen.objects.filter(estado='pendiente')
