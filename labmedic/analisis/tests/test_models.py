import pytest
from analisis.models import Analisis, PerfilAnalisis

@pytest.mark.django_db
def test_crear_analisis():
    analisis = Analisis.objects.create(
        nombre="Glucosa",
        descripcion="Medición de glucosa en sangre",
        unidad="mg/dL",
        precio=15.00,
        activo=True
    )
    assert analisis.nombre == "Glucosa"
    assert analisis.precio == 15.00
    assert analisis.activo is True

@pytest.mark.django_db
def test_crear_perfil_con_analisis():
    a1 = Analisis.objects.create(nombre="AST", unidad="U/L", precio=20)
    a2 = Analisis.objects.create(nombre="ALT", unidad="U/L", precio=25)
    perfil = PerfilAnalisis.objects.create(nombre="Perfil Hepático")
    perfil.analisis.set([a1, a2])
    assert perfil.analisis.count() == 2
