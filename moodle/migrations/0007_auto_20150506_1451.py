# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0006_auto_20150506_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(primary_key=True, to='moodle.Persona', parent_link=True, auto_created=True, serialize=False)),
                ('areaAsignada', models.CharField(max_length=50, help_text='Ingrese el area asignada')),
                ('calificacion', models.CharField(max_length=2)),
                ('certificado', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['fecha_nacimiento'],
            },
            bases=('moodle.persona',),
        ),
        migrations.CreateModel(
            name='MasterTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(primary_key=True, to='moodle.Persona', parent_link=True, auto_created=True, serialize=False)),
                ('experiencia', models.PositiveIntegerField(max_length=30, help_text='Ingrese el nombre del Usuario')),
            ],
            options={
                'ordering': ['fecha_nacimiento'],
            },
            bases=('moodle.persona',),
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={},
        ),
    ]
