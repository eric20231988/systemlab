from django import forms
from .models import Analito

class AnalitoForm(forms.ModelForm):
    class Meta:
        model = Analito
        fields = ['nombre', 'unidad', 'valor_minimo', 'valor_maximo', 'analisis', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'analisis': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
