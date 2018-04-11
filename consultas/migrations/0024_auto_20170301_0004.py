# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0023_remove_semestre_calendario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semestre',
            name='fecha_fin',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='fecha_inicio',
            field=models.CharField(max_length=10),
        ),
    ]
