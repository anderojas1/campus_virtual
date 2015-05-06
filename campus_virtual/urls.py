"""campus_virtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from moodle.views import CrearCurso, VerCurso, BorrarCurso, ListaCursos, EditarCurso


cursos_url = patterns ('',
	url(r'^nuevo-curso$', CrearCurso.as_view(), name = 'add_curso'),
    url(r'^$', VerCurso.as_view(), name = 'ver_curso'),
    url(r'^delete$', BorrarCurso.as_view(), name = 'borrar_curso'),
    url(r'^listados$', ListaCursos.as_view(), name = 'listado_cursos'),
    url(r'^update$', EditarCurso.as_view(), name = 'update_curso'),



)

urlpatterns = patterns ('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^curso/', include(cursos_url)),
    url(r'^(?P<slug>[\w-]+)/', include(cursos_url)),
)

