from django import forms
from .models import ResultadoAnalito

class ResultadoAnalitoForm(forms.ModelForm):
    class Meta:
        model = ResultadoAnalito
        fields = ['registro_examen', 'analito', 'valor']
        widgets = {
            'registro_examen': forms.Select(attrs={'class': 'form-select'}),
            'analito': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
