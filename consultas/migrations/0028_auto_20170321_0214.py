# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0027_auto_20170321_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='edificio',
            field=models.CharField(max_length=7, unique=True, null=True),
        ),
    ]
