from django import forms
from .models import Mascota, RegistroVacuna

RAZAS_PERRO = [
    ("", "Selecciona una raza"),
    ("Criollo", "Criollo"),
    ("Labrador", "Labrador"),
    ("Pastor Alemán", "Pastor Alemán"),
    ("Bulldog", "Bulldog"),
    ("Poodle", "Poodle"),
    ("Golden Retriever", "Golden Retriever"),
    ("Beagle", "Beagle"),
    ("Chihuahua", "Chihuahua"),
    ("Rottweiler", "Rottweiler"),
    ("Boxer", "Boxer"),
    ("Dálmata", "Dálmata"),
    ("Doberman", "Doberman"),
    ("Husky Siberiano", "Husky Siberiano"),
    ("Shih Tzu", "Shih Tzu"),
    ("Yorkshire Terrier", "Yorkshire Terrier"),
    ("Schnauzer", "Schnauzer"),
    ("Cocker Spaniel", "Cocker Spaniel"),
    ("French Bulldog", "French Bulldog"),
    ("Pitbull", "Pitbull"),
    ("Otro", "Otro"),
]

RAZAS_GATO = [
    ("", "Selecciona una raza"),
    ("Criollo", "Criollo"),
    ("Persa", "Persa"),
    ("Siamés", "Siamés"),
    ("Maine Coon", "Maine Coon"),
    ("Bengalí", "Bengalí"),
    ("Ragdoll", "Ragdoll"),
    ("Esfinge", "Esfinge"),
    ("Angora", "Angora"),
    ("Birmano", "Birmano"),
    ("Azul Ruso", "Azul Ruso"),
    ("Abisinio", "Abisinio"),
    ("Scotish Fold", "Scotish Fold"),
    ("British Shorthair", "British Shorthair"),
    ("Otro", "Otro"),
]


class MascotaForm(forms.ModelForm):
    raza = forms.ChoiceField(
        choices=[("", "Selecciona una raza")],
        widget=forms.Select(attrs={"class": "form-select"}),
        required=False,
    )

    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "fecha_nacimiento"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de la mascota"}
            ),
            "especie": forms.Select(attrs={"class": "form-select", "id": "id_especie"}),
            "fecha_nacimiento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.especie == "perro":
                self.fields["raza"].choices = RAZAS_PERRO
            else:
                self.fields["raza"].choices = RAZAS_GATO
        elif self.data.get("especie") == "perro":
            self.fields["raza"].choices = RAZAS_PERRO
        elif self.data.get("especie") == "gato":
            self.fields["raza"].choices = RAZAS_GATO
        else:
            self.fields["raza"].choices = [("", "Primero selecciona la especie")]


class RegistroVacunaForm(forms.ModelForm):
    class Meta:
        model = RegistroVacuna
        fields = ["vacuna", "fecha_aplicacion", "proxima_dosis", "veterinario", "notas"]
        widgets = {
            "vacuna": forms.Select(attrs={"class": "form-select"}),
            "fecha_aplicacion": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "proxima_dosis": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "veterinario": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del veterinario"}
            ),
            "notas": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Notas adicionales",
                }
            ),
        }
