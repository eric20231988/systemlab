from .models import RegistroExamen
import pandas as pd

def crear_registro_examen(data, user):
    return RegistroExamen.objects.create(**data, registrado_por=user)
def exportar_examenes_excel(queryset):
    df = pd.DataFrame(queryset.values('paciente', 'tipo_examen__nombre', 'estado', 'fecha_creacion'))
    # Aquí puedes generar el archivo Excel y devolverlo como respuesta HTTP
    return df