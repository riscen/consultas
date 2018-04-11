direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/horarioFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Horario

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter=',')

for fila in lectorDatos:
    horario = Horario(l=fila[0], m=fila[1], i=fila[2], j=fila[3], v=fila[4], s=fila[5])
    print(horario)
    horario.save()