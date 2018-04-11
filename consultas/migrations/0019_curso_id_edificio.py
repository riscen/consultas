# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0018_auto_20170216_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='id_edificio',
            field=models.ForeignKey(default=b'null', to='consultas.Edificio', null=True),
        ),
    ]
