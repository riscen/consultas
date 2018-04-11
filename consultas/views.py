from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from .models import Aula, Curso, Materia, Materia_Area, Curso_Horario, Semestre, Profesor, \
    Carrera, Curso_Carrera, User, Departamento, Edificio, Materia_Carrera
from .forms import SelectEdificioForm, UsuarioForm
from django.db.models import Q, F, Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    materias = Materia.objects.all()
    materiasSinRepetir = []
    for materia in materias:
        materiaValida = True
        if materiasSinRepetir:
            for mr in materiasSinRepetir:
                if mr.nombre_materia == materia.nombre_materia:
                    materiaValida = False
                    break
        if materiaValida:
            materiasSinRepetir.append(materia)
    dpto = Departamento.objects.all()
    size_dpto = len(dpto)
    edif = Edificio.objects.all()
    size_edif = len(edif)
    prof = Profesor.objects.all()
    size_prof = len(prof)
    size_mate = len(materiasSinRepetir)
    curs = Curso.objects.all()
    size_curs = len(curs)
    context = {
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id,
        'no_dpto': size_dpto,
        'no_edif': size_edif,
        'no_prof': size_prof,
        'no_mate': size_mate,
        'no_curs': size_curs
    }
    return render(request, 'consultas/index.html', context)

def consultar_horarios(request):
    if request.method == 'POST':
        formEdificio = SelectEdificioForm(request.POST)
        if formEdificio.is_valid():
            url = reverse('home')
            return HttpResponse('<h2>Funciono</h2>')
    else:
        formEdificio = SelectEdificioForm()
    context = {
        'formEdificio': formEdificio,
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id
    }
    return render(request, 'consultas/mostrarCursosEdificio.html', context)

def dameAulas(request):
    id_edificio = request.GET.get('id_edificio')
    aulas = Aula.objects.none()
    semestres = Semestre.objects.all()
    opciones = '<option value="" selected="selected">--------</option>'
    if id_edificio:
        aulas = Aula.objects.filter(id_edificio=id_edificio)
    for aula in aulas:
        opciones += '<option value=%s>%s</option>' % (
            aula.id,
            aula.aula
        )

    opcionesSemestre = '<option value="" selected="selected">--------</option>'
    calendarios = []
    for semestre in semestres:
        if not calendarios.__contains__(semestre.calendario):
            opcionesSemestre += '<option value="%s">%s</option>' % (
                semestre.id,
                semestre.calendario
            )
            calendarios.append(semestre.calendario)
    response = {}
    response['aulas'] = opciones
    response['semestres'] = opcionesSemestre;
    return JsonResponse(response)

def cargarCursos(request):
    idAula = request.GET.get('id_aula')
    idCalendario = request.GET.get('id_calendario')
    calendario = Semestre.objects.get(id=idCalendario).calendario

    tabla = '<thead>'
    tabla += '<tr><th>Hora/Día</th><th>Lunes</th><th>Martes</th><th>Miércoles</th><th>Jueves</th>' + \
             '<th>Viernes</th><th>Sábado</th></tr>'
    tabla += '</thead>'
    cursosHorario = Curso_Horario.objects.filter(id_aula=idAula, id_curso__id_semestre__calendario=calendario).order_by(
        'id_hora__hora_inicio', 'id_hora__hora_fin')

    if cursosHorario:
        horas = [hora for hora in range(700, 2200, 100)]
        dias = ['L', 'M', 'I', 'J', 'V', 'S']
        tabla += '<tbody>'
        for hora in horas:
            tabla += '<tr>'
            tabla += '<th>' + str(hora) + '</th>'
            for dia in dias:
                cursos = cursosHorario.filter(Q(id_horario__l=dia) | Q(id_horario__m=dia) | Q(id_horario__i=dia) |
                                              Q(id_horario__j=dia) | Q(id_horario__v=dia) | Q(id_horario__s=dia),
                                              id_hora__hora_inicio__lte=hora, id_hora__hora_fin__gte=hora)
                if(len(cursos) <= 1):
                    tabla += '<td class="">'
                else:
                    tabla += '<td class="success">'
                for curso in cursos:
                    tabla += '<br>'
                    tabla += '<a href="/consultas/curso/' + str(curso.id_curso.nrc) + '/">' + \
                             str(curso.id_curso.nrc) + ' ' + str(curso.id_curso.seccion) + '</a> '
                    tabla += '<br>'
                    tabla += '<a href="/consultas/materia/' + str(curso.id_curso.id_materia.id) + '/">'
                    tabla += curso.id_curso.id_materia.clave + ' '
                    tabla += curso.id_curso.id_materia.nombre_materia + ' '
                    tabla += '</a><br>'
                    profesor = curso.id_curso.id_profesor.apellidos
                    if(profesor == ''):
                        tabla += '[Sin profesor]'
                    else:
                        tabla += '<a href="/consultas/profesor/' + str(curso.id_curso.id_profesor.id) + '/">'
                        tabla += profesor + ', ' + curso.id_curso.id_profesor.nombres
                        tabla += '</a>'
                    tabla += '<br>'
                tabla += '</td>'
            tabla += '</tr>'
        tabla += '</tbody>'
    else:
        tabla = "No hay cursos"

    response = {}
    response['cursos'] = tabla
    return JsonResponse(response)

def mostrarInfoCursos(request, nrc):
    carreras = []
    curso = Curso.objects.get(nrc=nrc)
    if request.user.is_authenticated():
        carreras = Carrera.objects.filter(id_coordinador=request.user)
    cursoHorario = Curso_Horario.objects.filter(id_curso=curso)
    context = {
        'nrc': curso.nrc,
        'seccion': curso.seccion,
        'clave': curso.id_materia.clave,
        'materia': curso.id_materia.nombre_materia,
        'id_materia': curso.id_materia.id,
        'creditos': curso.id_materia.creditos,
        'profesor': str(curso.id_profesor.apellidos) + ', ' + str(curso.id_profesor.nombres),
        'id_profesor': curso.id_profesor.id,
        'depto': curso.id_materia.id_departamento.nombre_departamento,
        'area': Materia_Area.objects.get(id_materia=curso.id_materia).id_area.acronimo,
        'estatus': curso.estatus,
        'cursoHorario': cursoHorario,
        'cupos': curso.cupos,
        'ocupados': curso.ocupados,
        'disponibles': curso.disponibles,
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id,
        'carreras': carreras,
    }
    return render(request, 'consultas/infoCurso.html', context)

def consultarProfesor(request):
    profesores = Profesor.objects.all().order_by('apellidos')
    infoProfesor = []
    for profesor in profesores:
        if(profesor.codigo != 0):
            cargaProfesor = Curso_Horario.objects.filter(id_curso__id_profesor=profesor).aggregate(carga=Sum(F('id_hora__hora_fin')+
                                                                                                             45-F('id_hora__hora_inicio')))
            if(cargaProfesor.get('carga') != None):
                carga = cargaProfesor.get('carga')/100
            else:
                carga = 0
            if(carga >= 40):
                id_fila = "sobrecargado"
            else:
                id_fila = ""
            infoProfesor.append({
                'id_fila': id_fila,
                'id': profesor.id,
                'codigo': profesor.codigo,
                'apellidos': profesor.apellidos,
                'nombres': profesor.nombres,
                'carga': str(carga)})
    context = {
        'infoProfesor': infoProfesor,
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id
    }
    return render(request, 'consultas/mostrarProfesores.html', context=context)

def cargarProfesores(request):
    filtro = request.GET.get('filtro')
    profesores = Profesor.objects.all().order_by('apellidos')
    tabla = '<thead>'
    tabla += '<tr><th>Código</th><th>Apellidos</th><th>Nombres</th><th>Carga horaria</th></tr>'
    tabla += '</thead>'
    tabla += '<tbody>'
    for profesor in profesores:
        if(profesor.codigo != 0):
            cargaProfesor = Curso_Horario.objects.filter(id_curso__id_profesor=profesor).aggregate(carga=Sum(F('id_hora__hora_fin')+
                                                                                                             45-F('id_hora__hora_inicio')))
            if(cargaProfesor.get('carga') != None):
                carga = cargaProfesor.get('carga')/100
            else:
                carga = 0

            if((filtro == "sobrecarga" and carga >= 40) or filtro == "todos"):
                if (carga >= 40):
                    id = "success"
                else:
                    id = ""
                tabla += '<tr class="' + id + '">'
                tabla += '<td><a href="/consultas/profesor/' + str(profesor.id) + '/">' + \
                         str(profesor.codigo) + '</a></td>'
                tabla += '<td>' + profesor.apellidos + '</td>'
                tabla += '<td>' + profesor.nombres + '</td>'
                tabla += '<td>' + str(carga) + '</td>'
                tabla += '</tr>'
    tabla += '</tbody>'
    response = {}
    response['profesores'] = tabla
    return JsonResponse(response)

def mostrarInfoProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    cargaProfesor = Curso_Horario.objects.filter(id_curso__id_profesor=profesor).aggregate(
        carga=Sum(F('id_hora__hora_fin') +
                  45 - F('id_hora__hora_inicio'))).get('carga')/100
    cursos = Curso_Horario.objects.filter(id_curso__id_profesor=profesor)
    context = {
        'profesor': profesor,
        'cargaProfesor': cargaProfesor,
        'cursos': cursos,
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id
    }
    return render(request, 'consultas/infoProfesor.html', context)

def mostrarCursosDisponibles(request, lim_sup, indice):
    if indice == "1":
        cursos = Curso.objects.all().order_by('id_materia__nombre_materia')
    elif indice == "2":
        cursos = Curso.objects.filter(disponibles__gt=0).order_by('id_materia__nombre_materia')
    elif indice == "3":
        cursos = Curso.objects.filter(id_profesor__codigo=0).order_by('id_materia__nombre_materia')
    else:
        cursosHorario = Curso_Horario.objects.filter(id_aula__id_edificio__edificio='', id_aula__aula='').order_by(
            'id_curso__id_materia__nombre_materia')
        cursos = []
        for cursoHorario in cursosHorario:
            cursos.append(cursoHorario.id_curso)
    total = len(cursos)
    sup = int(lim_sup)
    if sup > 0 and total-(sup-100) > 0:
        cursos = cursos[(int(lim_sup)-100):int(lim_sup)]
        cursosDisponibles = []
        cursosRegistrados = []
        if request.user.is_authenticated():
            cursosRegistrados = Curso_Carrera.objects.filter(id_carrera__id_coordinador=request.user)
        for curso in cursos:
            clase = ""
            if cursosRegistrados:
                for cursoRegistrado in cursosRegistrados:
                    if cursoRegistrado.id_curso.nrc == curso.nrc:
                        clase = "success"
                        break
            cursosDisponibles.append({
                'clase': clase,
                'nrc': str(curso.nrc),
                'materia': str(curso.id_materia.nombre_materia),
                'id_materia': curso.id_materia.id,
                'area': Materia_Area.objects.get(id_materia__clave=curso.id_materia.clave),
                'seccion': str(curso.seccion),
                'profesor_apellidos': str(curso.id_profesor.apellidos),
                'profesor_nombres': str(curso.id_profesor.nombres),
                'id_profesor': curso.id_profesor.id,
                'disponibles': str(curso.disponibles)
            })
        inf = sup - 100
        sig = sup + 100
        if total-(sup-100) < 100:
            sup = total
        context = {
            'ant_sup': inf,
            'sup': sup,
            'sig_sup': sig,
            'total': total,
            'indice': int(indice),
            'cursos': cursosDisponibles,
            'sesion_iniciada': request.user.is_authenticated(),
            'id_usuario': request.user.id
        }
    else:
        cursos = []
        context = {
            'ant_sup': 0,
            'sup': 0,
            'sig_sup': 100,
            'total': total,
            'indice': int(indice),
            'cursos': cursos,
            'sesion_iniciada': request.user.is_authenticated(),
            'id_usuario': request.user.id
        }
    return render(request, 'consultas/mostrarCursos.html', context)

def cargarCursosEspecificados(request):
    filtro = 1
    if request.method == "POST":
        filtro = request.POST['filtro']
    return redirect('consultas:mostrarCursosDisponibles', 100, filtro)

def mostrarInfoMateria(request, id_materia):
    materia = Materia.objects.get(id=int(id_materia))
    cursos = Curso.objects.filter(id_materia__nombre_materia=materia.nombre_materia).order_by('id_materia__clave', 'nrc')
    infoCursos = []
    for curso in cursos:
        infoCursos.append({
            'nrc': curso.nrc,
            'clave': curso.id_materia.clave,
            'seccion': curso.seccion,
            'if_profesor': curso.id_profesor.id,
            'profesor': str(curso.id_profesor.apellidos) + ', ' + str(curso.id_profesor.nombres),
            'area': Materia_Area.objects.get(id_materia=curso.id_materia).id_area.acronimo,
            'semestre': curso.id_semestre.calendario,
            'estatus': curso.estatus
        })
    context = {
        'materia': materia,
        'cursos': infoCursos,
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id
    }
    return render(request, 'consultas/infoMateria.html', context)

def mostrarMaterias(request, lim_sup):
    materias = Materia.objects.all().order_by('nombre_materia')
    sup = int(lim_sup)
    infoMateria = []
    materiasSinRepetir = []
    for materia in materias:
        materiaValida = True
        if materiasSinRepetir:
            for mr in materiasSinRepetir:
                if mr.nombre_materia == materia.nombre_materia:
                    materiaValida = False
                    break
        if materiaValida:
            materiasSinRepetir.append(materia)
    total = len(materiasSinRepetir)
    if sup > 0 and total-(sup-100) > 0:
        materias = materiasSinRepetir[int(lim_sup)-100:int(lim_sup)]
        for materia in materias:
            infoMateria.append({
                'id': int(materia.id),
                'nombre_materia': str(materia.nombre_materia),
                'departamento': str(materia.id_departamento.nombre_departamento),
                'creditos': materia.creditos
            })
        inf = sup-100
        sig = sup + 100
        if total-(sup-100) < 100:
            sup = total
        context = {
            'ant_sup': inf,
            'sup': sup,
            'sig_sup': sig,
            'total': total,
            'materias': infoMateria,
            'sesion_iniciada': request.user.is_authenticated(),
            'id_usuario': request.user.id
        }
    else:
        context = {
            'ant_sup': 0,
            'sup': 0,
            'sig_sup': 100,
            'total': total,
            'materias': infoMateria,
            'sesion_iniciada': request.user.is_authenticated(),
            'id_usuario': request.user.id
        }
    return render(request, 'consultas/mostrarMaterias.html', context)

def cerrarSesion(request):
    logout(request)
    form = UsuarioForm(request.POST or None)
    context = {
        "form": form,
        'sesion_iniciada': False
    }
    return render(request, 'consultas/iniciar_sesion.html', context)


def iniciarSesion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'consultas/index.html', {'sesion_iniciada': True,
                                                                'id_usuario': user.id})
            else:
                return render(request, 'consultas/iniciar_sesion.html', {'error_message': 'Usuario no válido.'})
        else:
            return render(request, 'consultas/iniciar_sesion.html', {'error_message': 'Alguno de los campos no es válido.'})
    return render(request, 'consultas/iniciar_sesion.html')


def mostrarInfoPerfil(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    carreras = Carrera.objects.filter(id_coordinador=usuario)
    if carreras:
        es_coordinador = True
    else:
        es_coordinador = False
    context = {
        'usuario': usuario,
        'es_coordinador': es_coordinador,
        'carreras': carreras,
        'sesion_iniciada': True,
        'id_usuario': id_usuario
    }
    return render(request, 'consultas/perfil.html', context)

def cargarCursosRegistrados(request):
    cursos = Curso_Carrera.objects.filter(id_carrera=request.GET.get('carrera'))
    if cursos:
        tabla = '<thead>'
        tabla += '<tr><th>NRC</th><th>Materia</th><th>Departamento</th><th>Profesor</th></tr>'
        tabla += '</thead>'
        for curso in cursos:
            tabla += '<tr>'
            tabla += '<td><a href="/consultas/curso/' + str(curso.id_curso.nrc) + '/">'
            tabla += str(curso.id_curso.nrc) + '</a></td>'
            tabla += '<td><a href="/consultas/materia/' + str(curso.id_curso.id_materia.id) + '/">'
            tabla += str(curso.id_curso.id_materia.nombre_materia) + '</a></td>'
            tabla += '<td>' + str(curso.id_curso.id_materia.id_departamento.nombre_departamento) + '</td>'
            tabla += '<td><a href="/consultas/profesor/' + str(curso.id_curso.id_profesor.id) + '/">'
            tabla += str(curso.id_curso.id_profesor.apellidos) + ', ' + str(curso.id_curso.id_profesor.nombres) + \
                     '</a></td>'
            tabla += '</tr>'
    else:
        tabla = '<h3>No hay cursos registrados</h3>'
    response = {}
    response['carreras'] = tabla
    return JsonResponse(response)

def mostrarCursosDisponiblesCarrera(request, acronimo, lim_sup):
    materiasCarrera = Materia_Carrera.objects.filter(id_carrera__acronimo=acronimo)
    cursos = []
    for mC in materiasCarrera:
        cursosConCupo = Curso.objects.filter(disponibles__gt=0, id_materia=mC.id_materia)
        for cc in cursosConCupo:
            cursos.append(cc)
    total = len(cursos)
    sup = int(lim_sup)
    if sup > 0 and total-(sup-100) > 0:
        cursos = cursos[(int(lim_sup)-100):int(lim_sup)]
        cursosDisponibles = []
        cursosRegistrados = []
        if request.user.is_authenticated():
            cursosRegistrados = Curso_Carrera.objects.filter(id_carrera__id_coordinador=request.user)
        for curso in cursos:
            clase = ""
            if cursosRegistrados:
                for cursoRegistrado in cursosRegistrados:
                    if cursoRegistrado.id_curso.nrc == curso.nrc:
                        clase = "success"
                        break
            cursosDisponibles.append({
                'clase': clase,
                'nrc': str(curso.nrc),
                'materia': str(curso.id_materia.nombre_materia),
                'id_materia': curso.id_materia.id,
                'area': Materia_Area.objects.get(id_materia__clave=curso.id_materia.clave),
                'seccion': str(curso.seccion),
                'profesor_apellidos': str(curso.id_profesor.apellidos),
                'profesor_nombres': str(curso.id_profesor.nombres),
                'id_profesor': curso.id_profesor.id,
                'disponibles': str(curso.disponibles)
            })
        inf = sup - 100
        sig = sup + 100
        if total-(sup-100) < 100:
            sup = total
        context = {
            'ant_sup': inf,
            'sup': sup,
            'sig_sup': sig,
            'total': total,
            'acronimo': acronimo,
            'cursos': cursosDisponibles,
            'usuario': request.user,
            'sesion_iniciada': request.user.is_authenticated(),
            'id_usuario': request.user.id
        }
    else:
        cursos = []
        context = {
            'ant_sup': 0,
            'sup': 0,
            'sig_sup': 100,
            'total': total,
            'acronimo': acronimo,
            'cursos': cursos,
            'usuario': request.user,
            'sesion_iniciada': request.user.is_authenticated(),
            'id_usuario': request.user.id
        }
    return render(request, 'consultas/cursosDisponibles.html', context)

def mostrarCursosDisponiblesCarrera1(request):
    acronimo = 'N'
    if request.method == "POST":
        indice = request.POST['carrera']
        print(str(int(indice) - 1))
        carrera = Carrera.objects.get(id=indice);
        #carrera = Carrera.objects.filter(id_coordinador=request.user.id)[int(indice) - 1]
        acronimo = carrera.acronimo
    return redirect('consultas:mostrarCursosDisponiblesCarrera', acronimo, 100)


def mostrarMallaCurricular(request, acronimo):
    carreras = Carrera.objects.all()
    materiasCarrera = Materia_Carrera.objects.filter(id_carrera__acronimo=acronimo).order_by('id_materia__clave')
    materias = []
    for mc in materiasCarrera:
        materias.append(mc.id_materia)
    context = {
        'usuario': request.user,
        'sesion_iniciada': request.user.is_authenticated(),
        'id_usuario': request.user.id,
        'carreras': carreras,
        'materias': materias,
        'acronimo': acronimo
    }
    return render(request, 'consultas/mallaCurricular.html', context)

def mostrarMalla(request):
    acronimo = 'N'
    if request.method == "POST":
        id_carrera = request.POST['carrera']
        acronimo = Carrera.objects.get(id=id_carrera).acronimo
    return redirect('consultas:mostrarMallaCurricular', acronimo)

def registrarCurso(request, nrc):
    if request.method == "POST":
        curso = Curso.objects.get(nrc=nrc)
        if curso.estatus == 'I':
            #messages.info(request=request, message="No se puede registrar esta curso")
            print("No se puede registrar este curso")
            return mostrarInfoCursos(request, nrc)
        else:
            indice = request.POST['carrera']
            carrera = Carrera.objects.get(id=indice)
            #carrera = Carrera.objects.filter(id_coordinador=request.user.id)[int(indice)-1]
            materiasCarrera = Materia_Carrera.objects.all()
            curso = Curso.objects.get(nrc=nrc)
            cursoValido = False
            for cM in materiasCarrera:
                if cM.id_materia.clave == curso.id_materia.clave and not Curso_Carrera.objects.filter(id_curso=curso):
                        cursoValido = True
            if cursoValido:
                cursoCarrera = Curso_Carrera(id_curso=Curso.objects.get(nrc=nrc), id_carrera=carrera)
                cursoCarrera.save()
                messages.success(request, "Curso registrado")
            else:
                messages.warning(request, "El curso ya fue registrado o no pertenece a la malla curricular.")
    return redirect('consultas:mostrarInfoCursos', nrc)
