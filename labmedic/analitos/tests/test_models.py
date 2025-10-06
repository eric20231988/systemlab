import pytest
from analitos.models import Analito
from analisis.models import Analisis

@pytest.mark.django_db
def test_analito_str():
    analisis = Analisis.objects.create(nombre="Perfil Lipídico")
    analito = Analito.objects.create(
        nombre="Colesterol",
        unidad="mg/dL",
        valor_minimo=120,
        valor_maximo=200,
        analisis=analisis
    )
    assert str(analito) == "Colesterol (mg/dL)"
