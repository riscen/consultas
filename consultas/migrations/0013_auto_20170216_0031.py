# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0012_auto_20170215_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='id_edificio',
            field=models.ForeignKey(default=b'null', to='consultas.Edificio'),
        ),
    ]
