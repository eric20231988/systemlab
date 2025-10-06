import django_filters
from .models import TipoExamen

class TipoExamenFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    activo = django_filters.BooleanFilter(label="Activo")

    class Meta:
        model = TipoExamen
        fields = ['nombre', 'activo']
