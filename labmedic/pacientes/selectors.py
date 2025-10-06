# pacientes/selectors.py
from django.db.models import Q
from .models import Paciente

def pacientes_queryset(q: str = ''):
    qs = Paciente.objects.all().order_by('-id')
    if q:
        qs = qs.filter(
            Q(dni__icontains=q) |
            Q(nombres__icontains=q) |
            Q(apellidos__icontains=q)
        )
    return qs

def get_paciente_by_dni(dni: str):
    return Paciente.objects.filter(dni=dni).first()

def get_paciente(pk: int):
    return Paciente.objects.filter(pk=pk).first()
