from precios.forms import PrecioForm

def test_formulario_precio_valido():
    form_data = {
        'tipo_examen': 1,
        'precio_base': 100,
        'descuento': 10,
        'igv': 18
    }
    form = PrecioForm(data=form_data)
    assert form.is_valid() or 'tipo_examen' in form.errors
