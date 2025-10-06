from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.panel, name='panel'),
    path('buscar/', views.buscar_paciente, name='buscar_paciente'),   
]
