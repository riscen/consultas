direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/departamentoFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Departamento

import csv

lectorDatos = csv.reader(open(direccionCsv, encoding='ISO-8859-1'), delimiter=',')

for fila in lectorDatos:
    depto = Departamento(nombre_departamento=fila[0])
    print(depto)
    depto.save()