direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/nivel_materiaFinal.csv"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
from django.core.wsgi import get_wsgi_application
sys.path.append("/home/riscen/PycharmProjects/SiiauOferta/siiauoferta")
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.siiauoferta.settings'
application = get_wsgi_application()

from consultas.models import Materia, Nivel, Nivel_Materia

import csv

lectorDatos = csv.reader(open(direccionCsv, encoding="ISO-8859-1"), delimiter=',')

for fila in lectorDatos:
    nm = Nivel_Materia(id_materia=Materia.objects.get(clave=fila[0]),
                       id_nivel=Nivel.objects.get(nivel=fila[1]))
    print(nm)
    nm.save()