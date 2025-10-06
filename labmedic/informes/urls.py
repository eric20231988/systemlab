from django.urls import path
from . import views

app_name = 'informes'

urlpatterns = [
    path('', views.InformeListView.as_view(), name='listar'),
    path('crear/', views.InformeCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.InformeDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.InformeUpdateView.as_view(), name='editar'),
    path('<int:pk>/pdf/', views.generar_pdf_informe, name='generar_pdf'),
    path('<int:pk>/eliminar/', views.InformeDeleteView.as_view(), name='eliminar'),
    path('<int:pk>/enviar/', views.enviar_por_whatsapp, name='enviar_whatsapp'),


]
