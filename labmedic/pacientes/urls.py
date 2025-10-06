# pacientes/urls.py
from django.urls import path
from .views import (
    PacienteListView,
    PacienteDetailView,
    crear_paciente_view,
    editar_paciente_view,
    eliminar_paciente_view,
    tabla_pacientes,
    verificar_dni,
    panel_list_partial,   # 👈 importa la vista
)

app_name = 'pacientes'

urlpatterns = [
    path('', PacienteListView.as_view(), name='listar'),
    path('crear/', crear_paciente_view, name='crear'),
    path('<int:pk>/', PacienteDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', editar_paciente_view, name='editar'),
    path('<int:pk>/eliminar/', eliminar_paciente_view, name='eliminar'),
    path('tabla/', tabla_pacientes, name='tabla_pacientes'),
    path('verificar-dni/', verificar_dni, name='verificar_dni'),
    path('panel-list/', panel_list_partial, name='panel_list'),  # ✅ ahora sí existe
]

