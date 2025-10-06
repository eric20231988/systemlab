from django.urls import path
from . import views

app_name = 'especialidad'

urlpatterns = [
    path('', views.EspecialidadListView.as_view(), name='listar'),
    path('crear/', views.EspecialidadCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.EspecialidadDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.EspecialidadUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.EspecialidadDeleteView.as_view(), name='eliminar'),
]
