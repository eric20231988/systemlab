from django import forms
from ..models import PerfilAnalisis

class PerfilAnalisisForm(forms.ModelForm):
    class Meta:
        model = PerfilAnalisis
        fields = '__all__'
