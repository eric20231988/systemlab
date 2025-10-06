from ..models import PerfilAnalisis

def crear_perfil(data, analisis_ids):
    perfil = PerfilAnalisis.objects.create(**data)
    perfil.analisis.set(analisis_ids)
    return perfil
