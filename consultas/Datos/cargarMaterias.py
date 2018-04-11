direccionCsv = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/consultas/Datos/materiaFinal.txt"
direccionProyecto = "/home/riscen/PycharmProjects/SiiauOferta/siiauoferta/"

import sys
import os
sys.path.append(direccionProyecto)
os.environ['DJANGO_SETTINGS_MODULE'] = 'siiauoferta.settings'

from consultas.models import Materia, Departamento, Nivel, Nivel_Materia

import csv

lectorDatos = csv.reader(open(direccionCsv, encoding="ISO-8859-1"), delimiter='\t')
for fila in lectorDatos:
    materia = Materia(clave=fila[0], nombre_materia=fila[1],
                      hrs_teoria=fila[2], hrs_lab=fila[3],
                      creditos=fila[4],
                      id_departamento=Departamento.objects.get(nombre_departamento=fila[5]))
    print(materia)
    materia.save()