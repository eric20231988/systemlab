from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.PanelLaboratorioView.as_view(), name='panel'),
    path('analitos/', views.AnalitosListView.as_view(), name='analitos_listar'),
    path('analisis/', views.AnalisisListView.as_view(), name='analisis_listar'),
    path('examenes/', views.ExamenesListView.as_view(), name='examenes_listar'),
    path('resultados/', views.ResultadosListView.as_view(), name='resultados_listar'),
    path('ordenes/', views.OrdenExamenListView.as_view(), name='orden_examen_listar'),
]
