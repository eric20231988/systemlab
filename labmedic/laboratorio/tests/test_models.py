import pytest
from analitos.models import Analito

@pytest.mark.django_db
def test_creacion_analito():
    analito = Analito.objects.create(
        nombre="Glucosa",
        unidad="mg/dL",
        valor_minimo=70,
        valor_maximo=110,
        activo=True
    )
    assert analito.nombre == "Glucosa"
    assert analito.valor_minimo < analito.valor_maximo
    assert analito.activo is True
