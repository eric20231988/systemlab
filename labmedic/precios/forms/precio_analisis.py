# precios/forms/precio_analisis.py
from django import forms
from ..models import PrecioAnalisis

class PrecioAnalisisForm(forms.ModelForm):
    class Meta:
        model = PrecioAnalisis
        fields = '__all__'
