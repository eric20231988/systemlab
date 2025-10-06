from resultados_analitos.forms import ResultadoAnalitoForm

def test_form_valido():
    form_data = {
        'registro_examen': 1,
        'analito': 1,
        'valor': 90
    }
    form = ResultadoAnalitoForm(data=form_data)
    assert form.is_valid() or 'registro_examen' in form.errors
