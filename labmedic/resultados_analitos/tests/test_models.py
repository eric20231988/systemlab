import pytest
from resultados_analitos.models import ResultadoAnalito
from registrar_examenes.models import RegistroExamen
from analitos.models import Analito

@pytest.mark.django_db
def test_resultado_str():
    examen = RegistroExamen.objects.create(paciente="Luis", tipo_examen_id=1)
    analito = Analito.objects.create(nombre="Glucosa", unidad="mg/dL", valor_minimo=70, valor_maximo=110)
    resultado = ResultadoAnalito.objects.create(registro_examen=examen, analito=analito, valor=85)
    assert str(resultado) == "Luis - Glucosa"
