# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0021_curso_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso_horario',
            name='id_horairo',
        ),
        migrations.AddField(
            model_name='curso_horario',
            name='id_horario',
            field=models.ForeignKey(to='consultas.Horario', null=True),
        ),
        migrations.AlterField(
            model_name='curso_horario',
            name='id_aula',
            field=models.ForeignKey(to='consultas.Aula', null=True),
        ),
        migrations.AlterField(
            model_name='curso_horario',
            name='id_edificio',
            field=models.ForeignKey(to='consultas.Edificio', null=True),
        ),
        migrations.AlterField(
            model_name='curso_horario',
            name='id_hora',
            field=models.ForeignKey(to='consultas.Hora', null=True),
        ),
    ]
