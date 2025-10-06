import pytest
from informes.models import Informe
from registrar_examenes.models import RegistroExamen

@pytest.mark.django_db
def test_informe_str():
    examen = RegistroExamen.objects.create(paciente="Ana", tipo_examen_id=1)
    informe = Informe.objects.create(registro_examen=examen)
    assert "Ana" in str(informe)
