import django_filters
from .models import RegistroExamen

class RegistroExamenFilter(django_filters.FilterSet):
    paciente = django_filters.CharFilter(lookup_expr='icontains', label='Paciente')
    estado = django_filters.ChoiceFilter(choices=RegistroExamen._meta.get_field('estado').choices)
    fecha_creacion = django_filters.DateFromToRangeFilter(label='Rango de fechas')

    class Meta:
        model = RegistroExamen
        fields = ['paciente', 'estado', 'fecha_creacion']
