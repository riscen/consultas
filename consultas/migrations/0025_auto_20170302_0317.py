# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0024_auto_20170301_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='aula',
            field=models.CharField(max_length=5),
        ),
    ]
