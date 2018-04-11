# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0011_auto_20170215_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='id_edificio',
            field=models.ForeignKey(to='consultas.Edificio', null=True),
        ),
    ]
