import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_listar_analitos_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('analitos:listar')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Analitos' in response.content
