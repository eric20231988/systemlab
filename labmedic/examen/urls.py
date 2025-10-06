from django.urls import path
from .views.views_examen import (
    listar_examenes,
    crear_examen,
    detalle_examen,
    editar_examen,
    eliminar_examen,
)
from .views.export_views import exportar_examenes_pdf

app_name = 'examenes'

urlpatterns = [
    path('', listar_examenes, name='listar'),
    path('crear/', crear_examen, name='crear'),
    path('<int:pk>/', detalle_examen, name='detalle'),
    path('<int:pk>/editar/', editar_examen, name='editar'),
    path('<int:pk>/eliminar/', eliminar_examen, name='eliminar'),
    path('exportar/pdf/', exportar_examenes_pdf, name='exportar_pdf'),
]
