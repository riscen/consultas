# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 10:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0034_auto_20170403_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='id_coordinador',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
