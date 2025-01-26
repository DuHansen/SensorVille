from django import forms
from .models import FormularioModel

class FormularioForm(forms.ModelForm):
    class Meta:
        model = FormularioModel
        fields = ['name', 'value', 'date', 'file']  # Incluímos 'date' no formulário
        widgets = {
            'value': forms.NumberInput(attrs={'step': '0.01'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
