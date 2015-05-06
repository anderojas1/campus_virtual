from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .forms import CursoForm, PersonaForm, CohorteForm
from .models import Curso, Persona, Cohorte
from django.core.urlresolvers import reverse

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


class PersonaMixin(object):
	model = Persona
	def get_context_data(self, **kwargs):
		kwargs.update({'object_name':'Persona'})
		return kwargs

class PersonaFormMixin(PersonaMixin):
    form_class = PersonaForm
    template_name = 'moodle/object_form.html'

class ListaPersona(PersonaMixin, ListView):
    template_name = 'moodle/object_list.html'
    #context_object_name = 'listado'

class DetallesPersona(PersonaMixin, DetailView):
    pass

class CrearPersona(PersonaFormMixin, CreateView):
    pass

class EditarPersona(PersonaFormMixin, UpdateView):
    pass

class BorrarPersona(PersonaMixin, DeleteView):
	template_name = 'moodle/object_confirm_delete.html'
	def get_success_url(self):
		return reverse('listado-cursos')

class VerPersona(PersonaMixin, DetailView):
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




