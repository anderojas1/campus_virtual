from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Curso(models.Model):
	lista_areas = ((0,'Ciencias Naturales'), (1, 'Matemáticas'), (2, 'Humanidades'), (3, 'Ciencias Sociales'))
	slug = models.SlugField(max_length=30, primary_key=True)
	nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del curso")
	area = models.PositiveSmallIntegerField(choices=lista_areas, help_text="Escoja el área a la que pertenece")
	actividad_uno = models.TextField(max_length=200, help_text="Ingrese la descripción de la actividad uno")
	actividad_dos = models.TextField(max_length=200, help_text="Ingrese la descripción de la actividad dos")
	actividad_tres = models.TextField(max_length=200, help_text="Ingrese la descripción de la actividad tres")
	actividad_cuatro = models.TextField(max_length=200, help_text="Ingrese la descripción de la actividad cuatro")
	fecha_creacion = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['fecha_creacion']

	def __str__(self):
		return self.nombre

	@property
	def full_codigo(self):
		return u"%s %s" % (str(self.area), self.nombre)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.full_codigo)
		return super(Curso, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ('ver_curso', [self.slug])

	@models.permalink
	def get_update_url(self):
		return ('update_curso', [self.slug])

	@models.permalink
	def get_delete_url(self):
		return ('delete_curso', [self.slug])


class Persona(models.Model):
    lista_sexo = ((0, 'Femenino'), (1, 'Masculino'))
    cedula = models.SlugField(max_length = 30, primary_key = True, help_text="Ingrese el numero de Cedula del Usuario")
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del Usuario")
    apellidos = models.CharField(max_length=50, help_text="Ingrese el apellido del Usuario")
    sexo = models.PositiveSmallIntegerField(choices=lista_sexo, help_text="Escoja el sexo del usuario")
    email = models.EmailField(max_length=50, help_text="Ingrese el correo electronico del usuario")
    celular = models.CharField(max_length=30, null=True, blank=True, help_text="Ingrese el numero movil del usuario")
    fijo = models.CharField(max_length=30, null=True, blank=True, help_text="Ingrese el numero fijo del usuario")
    fecha_nacimiento = models.CharField(max_length=30, help_text="Ingrese la fecha de nacimiento del usuario")

    class Meta:
        ordering = ['fecha_nacimiento']

    @models.permalink
    def get_absolute_url(self):
        return ('ver_persona', [self.cedula])

    @models.permalink
    def get_update_url(self):
        return ('update_persona', [self.cedula])

    @models.permalink
    def get_delete_url(self):
        return ('delete_persona', [self.cedula])



