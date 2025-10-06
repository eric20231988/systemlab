import factory
from pacientes.models import Paciente

class PacienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Paciente
    tipo_documento = 'DNI'
    dni = factory.Sequence(lambda n: f'0000000{n}')
    nombres = 'Juan'
    apellidos = 'Pérez'
