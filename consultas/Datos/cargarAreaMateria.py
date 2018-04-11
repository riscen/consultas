direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/materia_areaFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
from django.core.wsgi import get_wsgi_application
sys.path.append("/home/riscen/PycharmProjects/SiiauOferta/siiauoferta")
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.siiauoferta.settings'
application = get_wsgi_application()

from consultas.models import Materia, Area, Materia_Area

import csv

lectorDatos = csv.reader(open(direccionCsv, encoding="ISO-8859-1"), delimiter=',')

for fila in lectorDatos:
    ma = Materia_Area(id_materia=Materia.objects.get(clave=fila[0]),
                       id_area=Area.objects.get(acronimo=fila[1]))
    print(ma)
    ma.save()