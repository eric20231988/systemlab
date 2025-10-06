from .models import Especialidad

def crear_especialidad(data):
    return Especialidad.objects.create(**data)

def actualizar_especialidad(especialidad, data):
    for key, value in data.items():
        setattr(especialidad, key, value)
    especialidad.save()
    return especialidad
