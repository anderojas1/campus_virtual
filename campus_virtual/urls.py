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
<<<<<<< HEAD
#<<<<<<< HEAD
from moodle.views import CrearMasterTeacher, VerMasterTeacher, BorrarMasterTeacher, ListaMasterTeacher, EditarMasterTeacher
from moodle.views import CrearLeaderTeacher, VerLeaderTeacher, BorrarLeaderTeacher, ListaLeaderTeacher, EditarLeaderTeacher
from moodle.views import CrearSecretariaEducacion, VerSecretariaEducacion, BorrarSecretariaEducacion, ListaSecretariaEducacion, EditarSecretariaEducacion
from moodle.views import CrearCurso, VerCurso, BorrarCurso, ListaCursos, EditarCurso
#>>>>>>> 543b6a7aed5fc02b6108860b03c313f09cbd59ef
=======
from moodle.views import CrearCurso, VerCurso, CrearPersona, VerPersona
from moodle.views import CrearCurso, VerCurso, BorrarCurso, ListaCursos, EditarCurso, VerCohorte, CrearCohorte
from moodle.views import BorrarCohorte, EditarCohorte, ListaCohorte
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a


cursos_url = patterns ('',
	url(r'^nuevo-curso$', CrearCurso.as_view(), name = 'add_curso'),
    url(r'^$', VerCurso.as_view(), name = 'ver_curso'),
<<<<<<< HEAD
    url(r'^delete-curso$', BorrarCurso.as_view(), name = 'borrar_curso'),
    url(r'^listados-curso$', ListaCursos.as_view(), name = 'listado_cursos'),
    url(r'^update-curso$', EditarCurso.as_view(), name = 'update_curso'),
=======
    url(r'^delete$', BorrarCurso.as_view(), name = 'borrar_curso'),
    url(r'^listados$', ListaCursos.as_view(), name = 'listado_cursos'),
    url(r'^update$', EditarCurso.as_view(), name = 'update_curso'),
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a

)

masterteacher_url =  patterns ('',
	url(r'^nuevo-master$', CrearMasterTeacher.as_view(), name = 'add_masterTeacher'),
    url(r'^$', VerMasterTeacher.as_view(), name = 'ver_masterTeacher'),
    url(r'^delete-master$', BorrarMasterTeacher.as_view(), name = 'borrar_masterTeacher'),
    url(r'^listados-master$', ListaMasterTeacher.as_view(), name = 'listado_masterTeacher'),
    url(r'^update-master$', EditarMasterTeacher.as_view(), name = 'update_masterTeacher'),

)

leaderteacher_url =  patterns ('',
	url(r'^nuevo-leader$', CrearLeaderTeacher.as_view(), name = 'add_leaderTeacher'),
    url(r'^$', VerLeaderTeacher.as_view(), name = 'ver_leaderTeacher'),
    url(r'^delete-leader$', BorrarLeaderTeacher.as_view(), name = 'borrar_leaderTeacher'),
    url(r'^listados-leader$', ListaLeaderTeacher.as_view(), name = 'listado_leaderTeacher'),
    url(r'^update-leader$', EditarLeaderTeacher.as_view(), name = 'update_leaderTeacher'),

)

secretaria_url = patterns ('',
	url(r'^nueva-secretaria$', CrearSecretariaEducacion.as_view(), name = 'add_secretaria'),
    url(r'^$', VerSecretariaEducacion.as_view(), name = 'ver_secretaria'),
    url(r'^delete-secretaria$', BorrarSecretariaEducacion.as_view(), name = 'borrar_secretaria'),
    url(r'^listados-secretaria$', ListaSecretariaEducacion.as_view(), name = 'listado_secretaria'),
    url(r'^update-secretaria$', EditarSecretariaEducacion.as_view(), name = 'update_secretaria'),

)

cohortes_url = patterns ('',
    url(r'^$', VerCohorte.as_view(), name='ver_cohorte'),
    url(r'^nueva-cohorte/$', CrearCohorte.as_view(), name='add_cohorte'),
    url(r'^delete$', BorrarCohorte.as_view(), name = 'borrar_cohorte'),
    url(r'^listados$', ListaCohorte.as_view(), name = 'listado_cohortes'),
    url(r'^update$', EditarCohorte.as_view(), name = 'update_cohorte'),
)

urlpatterns = patterns ('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^curso/', include(cursos_url)),
    url(r'^(?P<slug>[\w-]+)/', include(cursos_url)),

    url(r'^master/', include(masterteacher_url)),
    url(r'^(?P<cedula>[\w-]+)/', include(masterteacher_url)),

    url(r'^leader/', include(leaderteacher_url)),
    url(r'^(?P<cedula>[\w-]+)/', include(leaderteacher_url)),

<<<<<<< HEAD
    url(r'^secretaria/', include(secretaria_url)),
    url(r'^(?P<codigo>[\w-]+)/', include(secretaria_url)),
=======
    url(r'^cohorte/$', include(cohortes_url)),
    url(r'^cohorte/(?P<slug>[\w-]+)/', include(cohortes_url)),

#    url(r'^secretaria/', include(usuario_url)),
#    url(r'^(?P<cedula>[\w-]+)/', include(usuario_url)),
>>>>>>> cb98d727d484bcf9294aacb058334bc648cb923a

)

