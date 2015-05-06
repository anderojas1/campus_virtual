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
from moodle.views import CrearCurso, VerCurso, CrearPersona, VerPersona


cursos_url = patterns ('',
	url(r'^nuevo-curso$', CrearCurso.as_view(), name = 'add_curso'),
    url(r'^$', VerCurso.as_view(), name = 'ver_curso'),

)

masterteacher_url =  patterns ('',
	url(r'^nueva-persona$', CrearPersona.as_view(), name = 'add_masterTeacher'),
    url(r'^$', VerPersona.as_view(), name = 'ver_masterTeacher'),

)

leaderteacher_url =  patterns ('',
	url(r'^nueva-persona$', CrearPersona.as_view(), name = 'add_leaderTeacher'),
    url(r'^$', VerPersona.as_view(), name = 'ver_leaderTeacher'),

)

secretaria_url = patterns ('',
	url(r'^nueva-persona$', CrearPersona.as_view(), name = 'add_secretaria'),
    url(r'^$', VerPersona.as_view(), name = 'ver_secretaria'),

)

urlpatterns = patterns ('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^curso/', include(cursos_url)),
    url(r'^(?P<slug>[\w-]+)/', include(cursos_url)),

    url(r'^master/', include(masterteacher_url)),
    url(r'^(?P<cedula>[\w-]+)/', include(masterteacher_url)),

    url(r'^leader/', include(leaderteacher_url)),
    url(r'^(?P<cedula>[\w-]+)/', include(leaderteacher_url)),

#    url(r'^secretaria/', include(usuario_url)),
#    url(r'^(?P<cedula>[\w-]+)/', include(usuario_url)),

)

