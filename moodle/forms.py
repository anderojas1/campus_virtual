from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'area', 'actividad_uno', 'actividad_dos', 'actividad_tres', 'actividad_cuatro')