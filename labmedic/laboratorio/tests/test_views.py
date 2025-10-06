import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_panel_laboratorio_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('laboratorio:panel')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Panel de Laboratorio' in response.content

@pytest.mark.django_db
def test_analitos_list_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('laboratorio:analitos_listar')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Analitos Registrados' in response.content
