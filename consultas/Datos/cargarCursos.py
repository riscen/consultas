direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/cursoFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
from django.core.wsgi import get_wsgi_application
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.siiauoferta.settings'
application = get_wsgi_application()

from consultas.models import Curso, Materia, Profesor, Semestre

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter=',')

for fila in lectorDatos:
    try:
        id_profesor = Profesor.objects.get(codigo=fila[7])
    except Profesor.DoesNotExist:
        id_profesor = None
    try:
        id_semestre = Semestre.objects.get(fecha_inicio=fila[8], fecha_fin=fila[9])
    except Semestre.DoesNotExist:
        id_semestre = None
    curso = Curso(nrc=fila[0],
                  seccion=fila[1],
                  cupos=fila[2],
                  disponibles=fila[3],
                  ocupados=fila[4],
                  estatus=fila[5],
                  id_materia=Materia.objects.get(clave=fila[6]),
                  id_profesor=id_profesor,
                  id_semestre=id_semestre)
    print(curso)
    curso.save()