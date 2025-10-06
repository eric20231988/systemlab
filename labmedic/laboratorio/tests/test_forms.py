import pytest
from laboratorio.forms import AnalitoForm
from analitos.models import Analito

@pytest.mark.django_db
def test_analito_form_valid():
    form_data = {
        'nombre': 'Hemoglobina',
        'unidad': 'g/dL',
        'valor_minimo': 12,
        'valor_maximo': 16
    }
    form = AnalitoForm(data=form_data)
    assert form.is_valid()

def test_analito_form_invalid():
    form_data = {
        'nombre': '',
        'unidad': '',
        'valor_minimo': '',
        'valor_maximo': ''
    }
    form = AnalitoForm(data=form_data)
    assert not form.is_valid()
