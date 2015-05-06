# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0002_auto_20150506_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.SlugField(serialize=False, primary_key=True, help_text='Ingrese el numero de Cedula del Usuario', max_length=30)),
                ('nombre', models.CharField(help_text='Ingrese el nombre del Usuario', max_length=50)),
                ('apellidos', models.CharField(help_text='Ingrese el apellido del Usuario', max_length=50)),
                ('sexo', models.PositiveSmallIntegerField(help_text='Escoja el sexo del usuario', choices=[(0, 'Femenino'), (1, 'Masculino')])),
                ('email', models.EmailField(help_text='Ingrese el correo electronico del usuario', max_length=50)),
                ('celular', models.CharField(help_text='Ingrese el numero movil del usuario', blank=True, null=True, max_length=30)),
                ('fijo', models.CharField(help_text='Ingrese el numero fijo del usuario', blank=True, null=True, max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'ordering': ['fecha_nacimiento'],
            },
        ),
    ]
