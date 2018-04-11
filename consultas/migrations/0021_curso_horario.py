# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0020_auto_20170228_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso_Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_aula', models.ForeignKey(to='consultas.Aula')),
                ('id_curso', models.ForeignKey(to='consultas.Curso')),
                ('id_edificio', models.ForeignKey(to='consultas.Edificio')),
                ('id_hora', models.ForeignKey(to='consultas.Hora')),
                ('id_horairo', models.ForeignKey(to='consultas.Horario')),
            ],
        ),
    ]
