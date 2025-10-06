from django.urls import path
from . import views

app_name = 'analitos'

urlpatterns = [
    path('', views.AnalitoListView.as_view(), name='listar'),
    path('crear/', views.AnalitoCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.AnalitoDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.AnalitoUpdateView.as_view(), name='editar'),
]
