from ..models import Examen

def crear_examen(data):
    examen = Examen.objects.create(
        nombre=data['nombre'],
        categoria=data['categoria']
    )
    examen.analisis.set(data['analisis'])
    return examen

def editar_examen(examen, data):
    examen.nombre = data['nombre']
    examen.categoria = data['categoria']
    examen.analisis.set(data['analisis'])
    examen.save()
    return examen

def eliminar_examen(examen):
    examen.delete()
