import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_listar_precios_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('precios:listar')
    response = client.get(url)
    assert response.status_code == 200
