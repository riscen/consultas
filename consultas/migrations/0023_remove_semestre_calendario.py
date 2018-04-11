# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0022_auto_20170228_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='calendario',
        ),
    ]
