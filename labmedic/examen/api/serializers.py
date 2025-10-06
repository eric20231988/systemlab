from rest_framework import serializers
from examen.models import TipoExamen

class TipoExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExamen
        fields = ['id', 'nombre', 'descripcion', 'activo']
