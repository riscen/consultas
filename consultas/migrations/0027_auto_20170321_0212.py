# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0026_auto_20170320_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edificio', models.CharField(max_length=7, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='aula',
            name='edificio',
        ),
        migrations.AddField(
            model_name='aula',
            name='id_edificio',
            field=models.ForeignKey(to='consultas.Edificio', null=True),
        ),
    ]
