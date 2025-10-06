from ..models import PrecioAnalisis

def crear_precio(data):
    return PrecioAnalisis.objects.create(**data)

def editar_precio(instance, data):
    for field, value in data.items():
        setattr(instance, field, value)
    instance.save()
    return instance

def eliminar_precio(instance):
    instance.delete()

