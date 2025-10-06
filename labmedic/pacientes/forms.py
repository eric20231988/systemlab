# pacientes/forms.py
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'tipo_documento', 'dni', 'nombres', 'apellidos',
            'fecha_nacimiento', 'sexo', 'telefono', 'email', 'direccion',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (css + ' form-control').strip()
