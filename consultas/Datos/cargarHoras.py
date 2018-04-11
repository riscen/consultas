direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/horaFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Hora

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter=',')

for fila in lectorDatos:
    hora = Hora(hora_inicio=fila[0], hora_fin=fila[1])
    print(hora)
    hora.save()