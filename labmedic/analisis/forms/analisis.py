from django import forms
from ..models import Analisis

class AnalisisForm(forms.ModelForm):
    class Meta:
        model = Analisis
        fields = '__all__'
