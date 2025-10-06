# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pacientes.selectors import pacientes_queryset

@login_required
def panel(request):
    pacientes = pacientes_queryset('')  # 👈 ahora sí pasamos pacientes
    return render(request, 'dashboard/panel.html', {'pacientes': pacientes})

@login_required
def buscar_paciente(request):
    # Aquí puedes agregar lógica para buscar pacientes
    return render(request, 'dashboard/buscar_paciente.html')
