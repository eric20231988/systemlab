from ..models import CategoriaExamen

def crear_categoria(data):
    return CategoriaExamen.objects.create(**data)

def editar_categoria(categoria, data):
    for field, value in data.items():
        setattr(categoria, field, value)
    categoria.save()
    return categoria

def eliminar_categoria(categoria):
    categoria.delete()
