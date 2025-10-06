import pytest
from django.urls import reverse
from examen.models import TipoExamen

@pytest.mark.django_db
def test_listar_examenes(client):
    TipoExamen.objects.create(nombre="Bioquímico")
    response = client.get(reverse("listar_examenes"))
    assert response.status_code == 200
    assert "Bioquímico" in response.content.decode()

@pytest.mark.django_db
def test_crear_examen(client):
    response = client.post(reverse("crear_examen"), {
        "nombre": "Inmunológico",
        "descripcion": "Exámenes inmunológicos",
        "activo": True
    })
    assert response.status_code == 302
    assert TipoExamen.objects.filter(nombre="Inmunológico").exists()
