import pytest
from pacientes.forms import PacienteForm

@pytest.mark.django_db
def test_form_paciente_valido():
    form = PacienteForm(data={
        'tipo_documento': 'DNI',
        'dni': '87654321',
        'nombres': 'Ana',
        'apellidos': 'García',
        'email': 'ana@example.com'
    })
    assert form.is_valid()

@pytest.mark.django_db
def test_form_paciente_dni_obligatorio():
    form = PacienteForm(data={
        'tipo_documento': 'DNI',
        'dni': '',
        'nombres': 'SinDoc',
        'apellidos': 'Test',
    })
    assert not form.is_valid()
    assert 'dni' in form.errors
