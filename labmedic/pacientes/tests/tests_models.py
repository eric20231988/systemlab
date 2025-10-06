from django.test import TestCase
from pacientes.models import Paciente

class PacienteModelTest(TestCase):
    def test_str(self):
        p = Paciente.objects.create(dni='123', nombres='Ana', apellidos='Lopez')
        self.assertIn('Lopez, Ana (123)', str(p))
