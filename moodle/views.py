from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
<<<<<<< HEAD
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
#<<<<<<< HEAD
from .forms import CursoForm,MasterTeacherForm, LeaderTeacherForm, SecretariaEducacionForm
from .models import Persona, Curso, MasterTeacher, LeaderTeacher, SecretariaEducacion
#>>>>>>> 543b6a7aed5fc02b6108860b03c313f09cbd59ef
=======
from django.shortcuts import get_object_or_404
from .forms import CursoForm, PersonaForm, CohorteForm
from .models import Curso, Persona, Cohorte
from django.core.urlresolvers import reverse
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a

# Create your views here.
class CursoMixin(object):
	model = Curso
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Curso'})
		return kwargs

class CursoFormMixin(CursoMixin):
    form_class = CursoForm
    template_name = 'moodle/object_form.html'

class ListaCursos(CursoMixin, ListView):
    template_name = 'moodle/object_list.html'
    #context_object_name = 'cursos'
    #context_object_name = 'listado'

class DetallesCurso(CursoMixin, DetailView):
    pass

class CrearCurso(CursoFormMixin, CreateView):
    pass

class EditarCurso(CursoFormMixin, UpdateView):
    pass

class BorrarCurso(CursoMixin, DeleteView):
	template_name = 'moodle/object_confirm_delete.html'
	def get_success_url(self):
		return reverse('listado_cursos')

class VerCurso(CursoMixin, DetailView):
	"""template_name = 'moodle/detalle_curso.html'
    def get_queryset(self):
        self.codigo = get_object_or_404(Curso, codigo=self.kwargs['slug'])
        print(self.codigo)
        return super(VerCurso, self).get_queryset().filter(self.codigo)
    """

	pass


class MasterTeacherMixin(object):
	model = MasterTeacher
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'MasterTeacher'})
		return kwargs

class MasterTeacherFormMixin(MasterTeacherMixin):
    form_class = MasterTeacherForm
    template_name = 'moodle/object_form.html'

class ListaMasterTeacher(MasterTeacherMixin, ListView):
    template_name = 'moodle/object_list.html'
    #context_object_name = 'listado'

class DetallesMasterTeacher(MasterTeacherMixin, DetailView):
    pass

class CrearMasterTeacher(MasterTeacherMixin, CreateView):
    pass

class EditarMasterTeacher(MasterTeacherFormMixin, UpdateView):
    pass

class BorrarMasterTeacher(MasterTeacherMixin, DeleteView):
	template_name = 'moodle/object_confirm_delete.html'
	def get_success_url(self):
		return reverse('listado-cursos')

class VerMasterTeacher(MasterTeacherMixin, DetailView):
	"""template_name = 'moodle/detalle_curso.html'
    def get_queryset(self):
        self.codigo = get_object_or_404(Curso, codigo=self.kwargs['slug'])
        print(self.codigo)
        return super(VerCurso, self).get_queryset().filter(self.codigo)
    """

	pass


class LeaderTeacherMixin(object):
	model = LeaderTeacher
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'LeaderTeacher'})
		return kwargs

class LeaderTeacherFormMixin(LeaderTeacherMixin):
    form_class = LeaderTeacherForm
    template_name = 'moodle/object_form.html'

class ListaLeaderTeacher(LeaderTeacherMixin, ListView):
    template_name = 'moodle/object_list.html'
    #context_object_name = 'listado'

class DetallesLeaderTeacher(LeaderTeacherMixin, DetailView):
    pass

class CrearLeaderTeacher(LeaderTeacherMixin, CreateView):
    pass

class EditarLeaderTeacher(LeaderTeacherFormMixin, UpdateView):
    pass

class BorrarLeaderTeacher(LeaderTeacherMixin, DeleteView):
	template_name = 'moodle/object_confirm_delete.html'
	def get_success_url(self):
		return reverse('listado-cursos')

class VerLeaderTeacher(LeaderTeacherMixin, DetailView):
	"""template_name = 'moodle/detalle_curso.html'
    def get_queryset(self):
        self.codigo = get_object_or_404(Curso, codigo=self.kwargs['slug'])
        print(self.codigo)
        return super(VerCurso, self).get_queryset().filter(self.codigo)
    """

	pass

class CohorteMixin(object):
    model = Cohorte
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Cohorte'})
        return kwargs

class CohorteFormMixin(CohorteMixin):
    form_class = CohorteForm
    template_name = 'moodle/object_form.html'

class ListaCohorte(CohorteMixin, ListView):
    #template_name = 'moodle/object_list.html'
    #context_object_name = 'listado'
    pass

class DetallesCohorte(CohorteMixin, DetailView):
    pass

class CrearCohorte(CohorteFormMixin, CreateView):
    pass

class EditarCohorte(CohorteFormMixin, UpdateView):
    pass

class BorrarCohorte(CohorteMixin, DeleteView):
    template_name = 'moodle/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('listado-cohortes')

class VerCohorte(CohorteMixin, DetailView):
    """template_name = 'moodle/detalle_curso.html'
    def get_queryset(self):
        self.codigo = get_object_or_404(Curso, codigo=self.kwargs['slug'])
        print(self.codigo)
        return super(VerCurso, self).get_queryset().filter(self.codigo)
    """

    pass

# Create your views here.
class SecretariaEducacionMixin(object):
	model = SecretariaEducacion
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Curso'})
		return kwargs

class SecretariaEducacionFormMixin(SecretariaEducacionMixin):
    form_class = SecretariaEducacionForm
    template_name = 'moodle/object_form.html'

class ListaSecretariaEducacion(SecretariaEducacionMixin, ListView):
    template_name = 'moodle/object_list.html'
    #context_object_name = 'cursos'
    #context_object_name = 'listado'

class DetallesSecretariaEducacion(SecretariaEducacionMixin, DetailView):
    pass

class CrearSecretariaEducacion(SecretariaEducacionFormMixin, CreateView):
    pass

class EditarSecretariaEducacion(SecretariaEducacionFormMixin, UpdateView):
    pass

class BorrarSecretariaEducacion(SecretariaEducacionMixin, DeleteView):
	template_name = 'moodle/object_confirm_delete.html'
	def get_success_url(self):
		return reverse('listado_cursos')

class VerSecretariaEducacion(SecretariaEducacionMixin, DetailView):
	"""template_name = 'moodle/detalle_curso.html'
    def get_queryset(self):
        self.codigo = get_object_or_404(Curso, codigo=self.kwargs['slug'])
        print(self.codigo)
        return super(VerCurso, self).get_queryset().filter(self.codigo)
    """

	pass

