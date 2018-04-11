# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0019_curso_id_edificio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='id_aula',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_edificio',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_hora',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_horario',
        ),
    ]
