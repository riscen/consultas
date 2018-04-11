direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/areaFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Area

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter=',')

for fila in lectorDatos:
    area = Area(acronimo=fila[0])
    print(area)
    area.save()