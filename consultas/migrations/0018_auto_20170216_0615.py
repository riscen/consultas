# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0017_auto_20170216_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id_aula',
            field=models.ForeignKey(default=b'null', to='consultas.Aula', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_hora',
            field=models.ForeignKey(default=b'null', to='consultas.Hora', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_horario',
            field=models.ForeignKey(default=b'null', to='consultas.Horario', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_profesor',
            field=models.ForeignKey(default=b'null', to='consultas.Profesor', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id_semestre',
            field=models.ForeignKey(default=b'null', to='consultas.Semestre', null=True),
        ),
    ]
