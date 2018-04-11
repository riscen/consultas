# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_auto_20170215_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='aula',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='aula',
            name='id_edificio',
            field=models.ForeignKey(to='consultas.Edificio'),
        ),
    ]
