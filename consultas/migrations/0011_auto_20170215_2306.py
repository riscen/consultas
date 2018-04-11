# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0010_horas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Horas',
            new_name='Hora',
        ),
    ]
