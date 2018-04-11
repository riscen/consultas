from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Edificio(models.Model):
    edificio = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.edificio

class Aula(models.Model):
    aula = models.CharField(max_length=5, null=True)
    id_edificio = models.ForeignKey(Edificio, null=True)

    def __str__(self):
        return self.aula + ", " + str(self.id_edificio)

class Area(models.Model):
    acronimo = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.acronimo

class Profesor(models.Model):
    nombres = models.CharField(max_length=50, default='');
    apellidos = models.CharField(max_length=50, default='');
    codigo = models.IntegerField(unique=True, default=0);

    def __str__(self):
        return self.apellidos + ", " + self.nombres + " - " + str(self.codigo)

class Horario(models.Model):
    l = models.CharField(max_length=1, null=True)
    m = models.CharField(max_length=1, null=True)
    i = models.CharField(max_length=1, null=True)
    j = models.CharField(max_length=1, null=True)
    v = models.CharField(max_length=1, null=True)
    s = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.l + ", " + self.m + ", " + self.i + ", " + self.j + ", " + self.v + ", " + self.s

class Hora(models.Model):
    hora_inicio = models.IntegerField()
    hora_fin = models.IntegerField()

    def __str__(self):
        return str(self.hora_inicio) + " - " + str(self.hora_fin)

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_departamento

class Semestre(models.Model):
    fecha_inicio = models.CharField(max_length=10)
    fecha_fin = models.CharField(max_length=10)
    calendario = models.CharField(max_length=3, default='')

    def __str__(self):
        return self.fecha_inicio + ", " + self.fecha_fin + ", " + self.calendario

class Nivel(models.Model):
    nivel = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nivel

class Materia(models.Model):
    nombre_materia = models.CharField(max_length=100)
    clave = models.CharField(max_length=5)
    creditos = models.IntegerField(default=0)
    hrs_teoria = models.IntegerField(default=0)
    hrs_lab = models.IntegerField(default=0)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.clave + ", " + self.nombre_materia + ", " + str(self.creditos)

class Nivel_Materia(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_materia) + " - " + str(self.id_nivel)

class Materia_Area(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_materia) + ", " + str(self.id_area)

class Curso(models.Model):
    nrc = models.IntegerField()
    seccion = models.CharField(max_length=3)
    cupos = models.IntegerField()
    ocupados = models.IntegerField()
    disponibles = models.IntegerField()
    estatus = models.CharField(max_length=1, default='')
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, default='null')
    id_semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, null=True, default='null')

    def __str__(self):
        return str(self.nrc) + ", " + self.seccion + ", " + str(self.id_materia) + ", " + str(self.id_semestre)

class Curso_Horario(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_hora = models.ForeignKey(Hora, null=True)
    id_horario = models.ForeignKey(Horario, null=True)
    id_aula = models.ForeignKey(Aula, null=True)

    def __str__(self):
        return str(self.id_curso) + ", " + str(self.id_aula) + ", " + str(self.id_hora)


class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=4, unique=True)
    id_coordinador = models.ForeignKey(User, on_delete=models.SET_NULL, default="", null=True)

    def __str__(self):
        return str(self.nombre_carrera) + ' - ' + str(self.acronimo)

class Materia_Carrera(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_materia) + ', ' + str(self.id_carrera)

class Curso_Carrera(models.Model):
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_carrera.acronimo) + ' - ' + str(self.id_curso.id_materia.nombre_materia)