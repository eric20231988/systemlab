from django.urls import path
from . import views

app_name = 'resultados_analitos'

urlpatterns = [
    path('', views.ResultadoListView.as_view(), name='listar'),
    path('crear/', views.ResultadoCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.ResultadoDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.ResultadoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.ResultadoDeleteView.as_view(), name='eliminar'),
]
