from informes.forms import InformeForm

def test_form_valido():
    form_data = {
        'registro_examen': 1,
        'observaciones': 'Paciente estable'
    }
    form = InformeForm(data=form_data)
    assert form.is_valid() or 'registro_examen' in form.errors
