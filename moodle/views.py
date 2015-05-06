from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .forms import CursoForm
from .models import Curso


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
		return reverse('listado-cursos')

class VerCurso(CursoMixin, DetailView):
	"""template_name = 'moodle/detalle_curso.html'
    def get_queryset(self):
        self.codigo = get_object_or_404(Curso, codigo=self.kwargs['slug'])
        print(self.codigo)
        return super(VerCurso, self).get_queryset().filter(self.codigo)
    """

	pass