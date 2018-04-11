# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0014_auto_20170216_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='creditos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='materia',
            name='hrs_lab',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='materia',
            name='hrs_teoria',
            field=models.IntegerField(default=0),
        ),
    ]
