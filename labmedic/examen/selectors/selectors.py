from ..models import Examen, CategoriaExamen

def obtener_examenes():
    return Examen.objects.select_related('categoria').prefetch_related('analisis')

def obtener_examen_por_id(pk):
    return Examen.objects.select_related('categoria').prefetch_related('analisis').get(pk=pk)

def obtener_categorias():
    return CategoriaExamen.objects.all()
