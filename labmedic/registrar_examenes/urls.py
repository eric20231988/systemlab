from django.urls import path
from . import views

app_name = 'registrar_examenes'

urlpatterns = [
    path('', views.RegistroExamenListView.as_view(), name='listar_general'),
    path('<int:paciente_id>/', views.listar, name='listar'),

    path('crear/', views.RegistroExamenCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.RegistroExamenDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.RegistroExamenUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.RegistroExamenDeleteView.as_view(), name='eliminar'),
    path('exportar/', views.exportar_excel, name='exportar_excel'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
]
