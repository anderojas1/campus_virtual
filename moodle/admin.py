from django.contrib import admin
from .models import Curso, Persona, Cohorte

# Register your models here.
admin.site.register(Curso)
admin.site.register(Persona)
admin.site.register(Cohorte)