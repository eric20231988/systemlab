import pytest
from analisis.forms import AnalisisForm, PerfilAnalisisForm
from analisis.models import Analisis

@pytest.mark.django_db
def test_formulario_analisis_valido():
    form = AnalisisForm(data={
        "nombre": "Colesterol",
        "descripcion": "Medición de colesterol total",
        "unidad": "mg/dL",
        "precio": 18.50,
        "activo": True
    })
    assert form.is_valid()

@pytest.mark.django_db
def test_formulario_perfil_valido():
    a1 = Analisis.objects.create(nombre="HDL", unidad="mg/dL", precio=22)
    form = PerfilAnalisisForm(data={
        "nombre": "Perfil Lipídico",
        "descripcion": "Incluye HDL, LDL, triglicéridos",
        "analisis": [a1.id]
    })
    assert form.is_valid()
