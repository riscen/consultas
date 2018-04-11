# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='aula',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='id_edificio',
        ),
        migrations.RemoveField(
            model_name='edificio',
            name='id',
        ),
        migrations.AlterField(
            model_name='edificio',
            name='id_edificio',
            field=models.CharField(max_length=5, unique=True, serialize=False, primary_key=True),
        ),
    ]
