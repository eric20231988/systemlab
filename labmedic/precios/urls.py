# precios/urls.py
from django.urls import path
from .views.precio_views import *

app_name = 'precios'

urlpatterns = [
    path('', listar_precios, name='listar'),
    path('crear/', crear_precio, name='crear'),
    path('<int:pk>/', detalle_precio, name='detalle'),
    path('<int:pk>/editar/', editar_precio, name='editar'),
    path('<int:pk>/eliminar/', eliminar_precio, name='eliminar'),
]
