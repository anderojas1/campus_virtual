from django import forms
from .models import Curso, Persona, MasterTeacher, LeaderTeacher, SecretariaEducacion

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
        #('nombre', 'area', 'actividad_uno', 'actividad_dos', 'actividad_tres', 'actividad_cuatro')

class MasterTeacherForm(forms.ModelForm):
    class Meta:
        model = MasterTeacher
        fields = "__all__"
        #('cedula', 'nombre', 'apellidos', 'sexo', 'email', 'celular', 'fijo', 'fecha_nacimiento', 'experiencia')

class LeaderTeacherForm(forms.ModelForm):
    class Meta:
        model = LeaderTeacher
        fields = "__all__"
        #('cedula', 'nombre', 'apellidos', 'sexo', 'email', 'celular', 'fijo', 'fecha_nacimiento', 'area_asignada', 'calificacion', 'certificado')

class SecretariaEducacionForm(forms.ModelForm):
    class Meta:
        model = SecretariaEducacion
        fields = "__all__"