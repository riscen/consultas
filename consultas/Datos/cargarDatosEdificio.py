direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/edificio.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Edificio

import csv

lectorDatos = csv.reader(open(direccionCsv))

for fila in lectorDatos:
    edificio = Edificio(edificio=fila[0])
    print(edificio)
    edificio.save()