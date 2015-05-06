from django import forms
<<<<<<< HEAD
from .models import Curso, Persona, MasterTeacher, LeaderTeacher, SecretariaEducacion
=======
from .models import Curso, Persona, Cohorte
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
        #('nombre', 'area', 'actividad_uno', 'actividad_dos', 'actividad_tres', 'actividad_cuatro')

class MasterTeacherForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
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
=======
        model = Persona
        fields = ('cedula', 'nombre', 'apellidos', 'sexo', 'email', 'celular', 'fijo', 'fecha_nacimiento')

class CohorteForm(forms.ModelForm):
	class Meta:
		model = Cohorte
		fields = ('codigo_curso', 'grupo')
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a
