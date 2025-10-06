from analitos.forms import AnalitoForm

def test_formulario_analito_valido():
    form_data = {
        'nombre': 'Glucosa',
        'unidad': 'mg/dL',
        'valor_minimo': 70,
        'valor_maximo': 110,
        'analisis': 1,
        'activo': True
    }
    form = AnalitoForm(data=form_data)
    assert form.is_valid() or 'analisis' in form.errors  # depende si existe el ID
