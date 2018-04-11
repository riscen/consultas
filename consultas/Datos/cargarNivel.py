direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/nivelFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Nivel

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter='\t')

for fila in lectorDatos:
    nivel = Nivel(nivel=fila[0])
    print(nivel)
    nivel.save()