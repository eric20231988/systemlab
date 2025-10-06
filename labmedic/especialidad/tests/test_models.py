import pytest
from especialidad.models import Especialidad

@pytest.mark.django_db
def test_especialidad_str():
    esp = Especialidad.objects.create(nombre="Cardiología")
    assert str(esp) == "Cardiología"
