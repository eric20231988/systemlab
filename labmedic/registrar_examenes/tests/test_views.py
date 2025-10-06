import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_listar_registro_examenes(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('registrar_examenes:listar')
    response = client.get(url)
    assert response.status_code == 200
