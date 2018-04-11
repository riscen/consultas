# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_auto_20170215_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='aula',
            field=models.CharField(default=b'', max_length=4),
        ),
        migrations.AddField(
            model_name='aula',
            name='id_edificio',
            field=models.ForeignKey(default=b'', to='consultas.Edificio'),
        ),
    ]
