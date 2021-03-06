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

	def get_nombre(self):
		return self.nombre

	@models.permalink
	def get_absolute_url(self):
		return ('ver_curso', [self.slug])

	@models.permalink
	def get_update_url(self):
		return ('update_curso', [self.slug])

	@models.permalink
	def get_delete_url(self):
		return ('borrar_curso', [self.slug])


class Persona(models.Model):
    lista_sexo = ((0, 'Femenino'), (1, 'Masculino'))
    cedula = models.CharField(max_length = 30, primary_key = True, help_text="Ingrese el numero de Cedula del Usuario")
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del Usuario")
    apellidos = models.CharField(max_length=50, help_text="Ingrese el apellido del Usuario")
    sexo = models.PositiveSmallIntegerField(choices=lista_sexo, help_text="Escoja el sexo del usuario")
    email = models.EmailField(max_length=50, help_text="Ingrese el correo electronico del usuario")
    celular = models.CharField(max_length=30, null=True, blank=True, help_text="Ingrese el numero movil del usuario")
    fijo = models.CharField(max_length=30, null=True, blank=True, help_text="Ingrese el numero fijo del usuario")
    fecha_nacimiento = models.CharField(max_length=30, help_text="Ingrese la fecha de nacimiento del usuario")

    def __str__(self):
    	return self.nombre

    class Meta:
        ordering = ['cedula']

    @models.permalink
    def get_absolute_url(self):
        return ('ver_persona', [self.cedula])

    @models.permalink
    def get_update_url(self):
        return ('update_persona', [self.cedula])

    @models.permalink
    def  get_delete_url(self):
        return ('delete_persona', [self.cedula])

<<<<<<< HEAD
class MasterTeacher(Persona):
    experiencia = models.PositiveIntegerField()

    class Meta:
        ordering = ['cedula']

    @models.permalink
    def get_absolute_url(self):
        return ('ver_master', [self.cedula])

    @models.permalink
    def get_update_url(self):
        return ('update_master', [self.cedula])

    @models.permalink
    def  get_delete_url(self):
        return ('delete_master', [self.cedula])


class LeaderTeacher(Persona):
    area_asignada = models.CharField(max_length = 50)
    calificacion = models.CharField(max_length = 2)
    certificado = models.CharField(max_length = 50)

    class Meta:
        ordering = ['cedula']

    @models.permalink
    def get_absolute_url(self):
        return ('ver_leader', [self.cedula])

    @models.permalink
    def get_update_url(self):
        return ('update_leader', [self.cedula])

    @models.permalink
    def  get_delete_url(self):
        return ('delete_leader', [self.cedula])


class SecretariaEducacion(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 30)
    entidad_territorial = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    fijo = models.CharField(max_length = 30, null = True, blank = True)
    direccion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['codigo']

    @models.permalink
    def get_absolute_url(self):
        return ('ver_secretaria', [self.codigo])

    @models.permalink
    def get_update_url(self):
        return ('update_secretaria', [self.codigo])

    @models.permalink
    def get_delete_url(self):
        return ('delete_secretaria', [self.codigo])
=======
class Cohorte(models.Model):
	codigo_curso = models.ForeignKey(Curso)
	slug = models.SlugField(primary_key = True, max_length=30)
	grupo = models.PositiveSmallIntegerField()

	@property
	def full_codigo(self):
		return u"%s %s" % (self.codigo_curso, str(self.grupo))

	def save(self, *args, **kwargs):
		self.slug = slugify(self.full_codigo)
		return super(Cohorte, self).save(*args, **kwargs)

	def __str__(self):
		return self.slug

	@models.permalink
	def get_absolute_url(self):
		return ('ver_cohorte', [self.slug])

	@models.permalink
	def get_update_url(self):
		return ('update_cohorte', [self.slug])

	@models.permalink
	def get_delete_url(self):
		return ('borrar_cohorte', [self.slug])
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a
