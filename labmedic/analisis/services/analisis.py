from ..models import Analisis

def crear_analisis(data):
    return Analisis.objects.create(**data)

def editar_analisis(instance, data):
    for field, value in data.items():
        setattr(instance, field, value)
    instance.save()
    return instance

def eliminar_analisis(instance):
    if not instance.perfiles.exists():
        instance.delete()
        return True
    return False
