import django

#direccionCsv = "C:\\Users\Riscen\Documents\DjangoProjects\siiauoferta\consultas\Datos\inco.csv"
#direccionCsv = "C:\\Users\Riscen\Documents\DjangoProjects\siiauoferta\consultas\Datos\COM.txt"
#direccionCsv = "C:\\Users\Riscen\Documents\DjangoProjects\siiauoferta\consultas\Datos\INNI.txt"
direccionCsv = "C:\\Users\Riscen\Documents\DjangoProjects\siiauoferta\consultas\Datos\LQFB.txt"
direccionProyecto = "C:\\Users\Riscen\Documents\DjangoProjects\siiauoferta"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'
django.setup()

from consultas.models import Materia, Carrera, Materia_Carrera

import csv

lectorDatos = csv.reader(open(direccionCsv, encoding="ISO-8859-1"), delimiter='\t')
for fila in lectorDatos:
    try:
        materia = Materia.objects.get(clave=fila[2])
    except Materia.DoesNotExist:
        materia = None
    if materia != None:
        mc = Materia_Carrera(id_carrera=Carrera.objects.get(acronimo=fila[0]),
                             id_materia=materia)
        print(mc)
        mc.save()