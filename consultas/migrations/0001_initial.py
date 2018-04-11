# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aula', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_edificio', models.CharField(unique=True, max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='id_edificio',
            field=models.ForeignKey(to='consultas.Edificio'),
        ),
    ]
