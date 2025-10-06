from django.test import TestCase
from django.urls import reverse

class PacientesViewsTest(TestCase):
    def test_list_url(self):
        url = reverse('pacientes:listar')
        self.assertTrue(url)
