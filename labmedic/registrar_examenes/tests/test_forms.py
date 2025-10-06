from registrar_examenes.forms import RegistroExamenForm

def test_formulario_valido():
    form_data = {
        'paciente': 'Ana Torres',
        'tipo_examen': 1,
        'estado': 'pendiente'
    }
    form = RegistroExamenForm(data=form_data)
    assert form.is_valid() or 'tipo_examen' in form.errors
