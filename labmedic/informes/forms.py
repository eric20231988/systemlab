from django import forms
from .models import Informe

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['registro_examen', 'observaciones']
        widgets = {
            'registro_examen': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
