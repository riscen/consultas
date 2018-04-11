direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/curso_horarioFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
from django.core.wsgi import get_wsgi_application
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.siiauoferta.settings'
application = get_wsgi_application()

from consultas.models import Curso_Horario, Curso, Hora, Horario, Aula, Edificio

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter=',')
i = 0
for fila in lectorDatos:
    #if(i > 2811):
    try:
        horaInicio=fila[1]
        horaFin=fila[2]
        if(horaInicio == ''):
            horaInicio = 0
        if(horaFin == ''):
            horaFin = 0
        id_hora = Hora.objects.get(hora_inicio=horaInicio, hora_fin=horaFin)
    except Hora.DoesNotExist:
        id_hora = None
    try:
        id_horario = Horario.objects.get(l=fila[3], m=fila[4],
                                         i=fila[5], j=fila[6],
                                         v=fila[7], s=fila[8])
    except Horario.DoesNotExist:
        id_horario = None
    try:
        id_edificio = Edificio.objects.get(edificio=fila[9])
    except Edificio.DoesNotExist:
        id_edificio = None
    try:
        id_aula = Aula.objects.get(aula=fila[10], id_edificio=id_edificio)
    except Aula.DoesNotExist:
        id_aula = None
    ch = Curso_Horario(id_curso=Curso.objects.get(nrc=fila[0]),
                       id_hora=id_hora,
                       id_horario=id_horario,
                       id_aula=id_aula
                       )
    print(ch)
    ch.save()
    #i = i+1