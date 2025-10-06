import pytest
from precios.models import Precio
from examen.models import TipoExamen

@pytest.mark.django_db
def test_precio_final():
    tipo = TipoExamen.objects.create(nombre="Hemograma")
    precio = Precio.objects.create(tipo_examen=tipo, precio_base=100, descuento=10, igv=18)
    assert precio.precio_final() == 106.2
