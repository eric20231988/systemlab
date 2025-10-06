from django.urls import path
from .views import *


app_name = 'analisis'

urlpatterns = [
    path('', listar_analisis, name='listar_analisis'),
    path('crear/', crear_analisis, name='crear_analisis'),
    path('<int:pk>/', detalle_analisis, name='detalle_analisis'),
    path('<int:pk>/editar/', editar_analisis, name='editar_analisis'),
    path('<int:pk>/eliminar/', eliminar_analisis, name='eliminar_analisis'),
    path('perfiles/', listar_perfiles, name='listar_perfiles'),
    path('perfiles/crear/', crear_perfil, name='crear_perfil'),
    path('perfiles/<int:pk>/', detalle_perfil, name='detalle_perfil'),
    path('perfiles/<int:pk>/editar/', editar_perfil, name='editar_perfil'),
    path('perfiles/<int:pk>/eliminar/', eliminar_perfil, name='eliminar_perfil'),
    path('exportar/pdf/', exportar_analisis_pdf, name='exportar_pdf'),
    path('exportar/excel/', exportar_perfiles_excel, name='exportar_excel'),
]
