# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0025_auto_20170302_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia_Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_area', models.ForeignKey(to='consultas.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='aula',
            name='id_edificio',
        ),
        migrations.RemoveField(
            model_name='curso_horario',
            name='id_edificio',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='estatus',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='id_area',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='id_nivel',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='info_profesor',
        ),
        migrations.AddField(
            model_name='aula',
            name='edificio',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='estatus',
            field=models.CharField(default=b'', max_length=1),
        ),
        migrations.AddField(
            model_name='profesor',
            name='apellidos',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='profesor',
            name='codigo',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='nombres',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='semestre',
            name='calendario',
            field=models.CharField(default=b'', max_length=3),
        ),
        migrations.AlterField(
            model_name='aula',
            name='aula',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='nivel',
            field=models.CharField(unique=True, max_length=2),
        ),
        migrations.DeleteModel(
            name='Edificio',
        ),
        migrations.AddField(
            model_name='nivel_materia',
            name='id_materia',
            field=models.ForeignKey(to='consultas.Materia'),
        ),
        migrations.AddField(
            model_name='nivel_materia',
            name='id_nivel',
            field=models.ForeignKey(to='consultas.Nivel'),
        ),
        migrations.AddField(
            model_name='materia_area',
            name='id_materia',
            field=models.ForeignKey(to='consultas.Materia'),
        ),
    ]
