import pytest
from examen.models import TipoExamen

@pytest.mark.django_db
def test_crear_tipo_examen():
    examen = TipoExamen.objects.create(nombre="Bioquímico", descripcion="Exámenes bioquímicos")
    assert examen.nombre == "Bioquímico"
    assert examen.activo is True
