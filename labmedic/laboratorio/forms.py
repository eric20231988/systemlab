from django import forms
from analitos.models import Analito
from analisis.models import Analisis
from examen.models import TipoExamen
from resultados_analitos.models import ResultadoAnalito

class AnalitoForm(forms.ModelForm):
    class Meta:
        model = Analito
        fields = ['nombre', 'unidad', 'valor_minimo', 'valor_maximo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = ResultadoAnalito
        fields = ['registro_examen', 'analito', 'valor']
        widgets = {
            'registro_examen': forms.Select(attrs={'class': 'form-select'}),
            'analito': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
