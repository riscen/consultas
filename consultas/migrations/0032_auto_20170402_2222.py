# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0031_auto_20170402_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='id_coordinador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='consultas.Coordinador'),
        ),
    ]
