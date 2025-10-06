import pytest
from registrar_examenes.models import RegistroExamen
from examen.models import TipoExamen

@pytest.mark.django_db
def test_registro_examen_str():
    tipo = TipoExamen.objects.create(nombre="Hemograma")
    registro = RegistroExamen.objects.create(paciente="Juan Pérez", tipo_examen=tipo)
    assert str(registro) == "Juan Pérez - Hemograma"
