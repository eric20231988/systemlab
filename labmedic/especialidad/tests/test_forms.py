from especialidad.forms import EspecialidadForm

def test_form_especialidad_valido():
    form_data = {'nombre': 'Urología', 'descripcion': 'Tracto urinario', 'activa': True}
    form = EspecialidadForm(data=form_data)
    assert form.is_valid()
