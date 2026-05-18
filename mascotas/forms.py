from django import forms
from .models import Mascota, RegistroVacuna


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza (opcional)'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class RegistroVacunaForm(forms.ModelForm):
    class Meta:
        model = RegistroVacuna
        fields = ['vacuna', 'fecha_aplicacion', 'proxima_dosis', 'veterinario', 'notas']
        widgets = {
            'vacuna': forms.Select(attrs={'class': 'form-select'}),
            'fecha_aplicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proxima_dosis': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'veterinario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del veterinario'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notas adicionales'}),
        }
