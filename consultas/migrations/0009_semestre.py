# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0008_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.CharField(unique=True, max_length=10)),
                ('fecha_fin', models.CharField(unique=True, max_length=10)),
                ('calendario', models.CharField(unique=True, max_length=5)),
            ],
        ),
    ]
