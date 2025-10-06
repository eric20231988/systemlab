from .models import Informe

def crear_informe_desde_resultados(registro_examen, observaciones=''):
    return Informe.objects.create(registro_examen=registro_examen, observaciones=observaciones)
