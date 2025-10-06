from rest_framework import viewsets
from examen.models import TipoExamen
from .serializers import TipoExamenSerializer
from rest_framework.permissions import IsAuthenticated

class TipoExamenViewSet(viewsets.ModelViewSet):
    queryset = TipoExamen.objects.all()
    serializer_class = TipoExamenSerializer
    permission_classes = [IsAuthenticated]
