# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0006_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('l', models.CharField(max_length=1, null=True)),
                ('m', models.CharField(max_length=1, null=True)),
                ('i', models.CharField(max_length=1, null=True)),
                ('j', models.CharField(max_length=1, null=True)),
                ('v', models.CharField(max_length=1, null=True)),
                ('s', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]
