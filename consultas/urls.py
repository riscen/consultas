from django.conf.urls import include, url
from . import views

app_name = 'consultas'

urlpatterns = [
    # /consultas
    url(r'^$', views.index, name='index'),

    url(r'^iniciar_sesion/$', views.iniciarSesion, name='iniciar_sesion'),
    url(r'^cerrar_sesion/$', views.cerrarSesion, name='cerrar_sesion'),

    # /consultas/consultar_horarios
    url(r'^consultar_horarios/$', views.consultar_horarios, name='consulta_horarios'),
    url(r'cargarCursos/$', views.cargarCursos, name='cargarCursos'),
    url(r'dameAulas/$', views.dameAulas, name='dameAulas'),

    # /consultas/cursos_disponibles/
    url(r'^curso/cursos/(?P<lim_sup>[0-9]+)/(?P<indice>[1-4])/$', views.mostrarCursosDisponibles, name='mostrarCursosDisponibles'),
    url(r'^cargarCursosEspecificados/$', views.cargarCursosEspecificados, name='cargarCursosEspecificados'),
    # /consultas/curso/[nrc]
    url(r'^curso/(?P<nrc>[0-9]+)/$', views.mostrarInfoCursos, name='mostrarInfoCursos'),
    url(r'^registrarCurso/(?P<nrc>[0-9]+)/$', views.registrarCurso, name='registrarCurso'),

    # /consultas/materia/[clave]
    url(r'^materia/(?P<id_materia>[0-9]+)/$', views.mostrarInfoMateria, name='mostrarInfoMateria'),
    # /consultas/materia/materias/
    url(r'^materia/materias/(?P<lim_sup>[0-9]+)/$', views.mostrarMaterias, name='mostrarMaterias'),

    # /consultas/profesor/[id]
    url(r'^profesor/(?P<id_profesor>[0-9]+)/$', views.mostrarInfoProfesor, name='mostrarInfoProfesor'),

    # /consultas/profesor/todos
    url(r'^profesor/$', views.consultarProfesor, name='consultarProfesor'),
    url(r'^cargarProfesores/$', views.cargarProfesores, name='cargarProfesores'),

    # /consultas/perfil/[id]
    url(r'^perfil/(?P<id_usuario>[0-9]+)/$', views.mostrarInfoPerfil, name='mostrarInfoPerfil'),
    url(r'^cargarCursosRegistrados/$', views.cargarCursosRegistrados, name='cargarCursosRegistrados'),
    url(r'^curso/cursos_disponibles/(?P<acronimo>[A-Z]+)/(?P<lim_sup>[0-9]+)/$', views.mostrarCursosDisponiblesCarrera,
        name='mostrarCursosDisponiblesCarrera'),
    url(r'^curso/cursos_disponibles/$', views.mostrarCursosDisponiblesCarrera1,
        name='mostrarCursosDisponiblesCarrera1'),
    url(r'^mallaCurricular/(?P<acronimo>[A-Z]+)/$', views.mostrarMallaCurricular, name='mostrarMallaCurricular'),
    url(r'^mallaCurricular/$', views.mostrarMalla, name='mostrarMalla'),
]