from django import forms
from .models import Curso, Persona

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'area', 'actividad_uno', 'actividad_dos', 'actividad_tres', 'actividad_cuatro')

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('cedula', 'nombre', 'apellidos', 'sexo', 'email', 'celular', 'fijo', 'fecha_nacimiento')