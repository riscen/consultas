# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0015_auto_20170216_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrc', models.IntegerField()),
                ('seccion', models.CharField(max_length=3)),
                ('cupos', models.IntegerField()),
                ('ocupados', models.IntegerField()),
                ('disponibles', models.IntegerField()),
                ('id_aula', models.ForeignKey(to='consultas.Aula')),
                ('id_hora', models.ForeignKey(to='consultas.Hora')),
                ('id_horario', models.ForeignKey(to='consultas.Horario')),
                ('id_materia', models.ForeignKey(to='consultas.Materia')),
                ('id_profesor', models.ForeignKey(to='consultas.Profesor')),
                ('id_semestre', models.ForeignKey(to='consultas.Semestre')),
            ],
        ),
    ]
