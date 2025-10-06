from django import forms
from django_select2.forms import Select2Widget
from .models import RegistroExamen

class RegistroExamenForm(forms.ModelForm):
    class Meta:
        model = RegistroExamen
        fields = ['paciente', 'tipo_examen', 'estado']
        widgets = {
            'paciente': forms.TextInput(attrs={'class': 'form-control select2'}),
            'tipo_examen': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
