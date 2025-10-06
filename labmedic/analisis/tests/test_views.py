import pytest
from django.urls import reverse
from analisis.models import Analisis

@pytest.mark.django_db
def test_listar_analisis(client):
    Analisis.objects.create(nombre="Glucosa", unidad="mg/dL", precio=15)
    url = reverse("listar_analisis")
    response = client.get(url)
    assert response.status_code == 200
    assert "Glucosa" in response.content.decode()

@pytest.mark.django_db
def test_crear_analisis_view(client):
    url = reverse("crear_analisis")
    data = {
        "nombre": "Creatinina",
        "unidad": "mg/dL",
        "precio": 12.00,
        "activo": True
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Analisis.objects.filter(nombre="Creatinina").exists()
