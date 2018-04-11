# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0016_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id_aula',
            field=models.ForeignKey(to='consultas.Aula', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_hora',
            field=models.ForeignKey(to='consultas.Hora', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_horario',
            field=models.ForeignKey(to='consultas.Horario', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_profesor',
            field=models.ForeignKey(to='consultas.Profesor', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_semestre',
            field=models.ForeignKey(to='consultas.Semestre', null=True),
        ),
    ]
