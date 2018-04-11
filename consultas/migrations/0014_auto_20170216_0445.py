# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0013_auto_20170216_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_materia', models.CharField(max_length=100)),
                ('estatus', models.CharField(max_length=1)),
                ('clave', models.CharField(max_length=5)),
                ('id_area', models.ForeignKey(to='consultas.Area')),
                ('id_departamento', models.ForeignKey(to='consultas.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(unique=True, max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='id_nivel',
            field=models.ForeignKey(to='consultas.Nivel'),
        ),
    ]
