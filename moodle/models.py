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
		return ('borrar_curso', [self.slug])


