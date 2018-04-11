direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/aulaFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Edificio, Aula

import csv

lectorDatos = csv.reader(open(direccionCsv), delimiter=',')

for fila in lectorDatos:
    try:
        id_edificio = Edificio.objects.get(edificio=fila[1])
    except Edificio.DoesNotExist:
        id_edificio = None
    aula = Aula(aula=fila[0], id_edificio=id_edificio)
    print(aula)
    aula.save()