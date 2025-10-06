from .models import Analito

def crear_analito(data):
    analito = Analito.objects.create(**data)
    return analito

def actualizar_analito(analito, data):
    for key, value in data.items():
        setattr(analito, key, value)
    analito.save()
    return analito
