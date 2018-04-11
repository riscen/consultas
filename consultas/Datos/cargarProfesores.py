direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/profesorFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Profesor

import csv

lectorDatos = csv.reader(open(direccionCsv, encoding='ISO-8859-1'), delimiter=',')

for fila in lectorDatos:
    profesor = Profesor(nombres=fila[0], apellidos=fila[1], codigo=fila[2])
    print(profesor)
    profesor.save()