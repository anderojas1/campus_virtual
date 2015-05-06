# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.SlugField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, help_text='Ingrese el nombre del curso')),
                ('area', models.PositiveSmallIntegerField(choices=[(0, 'Ciencias Naturales'), (1, 'Matemáticas'), (2, 'Humanidades'), (3, 'Ciencias Sociales')], help_text='Escoja el área a la que pertenece')),
                ('actividad_uno', models.TextField(max_length=200, help_text='Ingrese la descripción de la actividad uno')),
                ('actividad_dos', models.TextField(max_length=200, help_text='Ingrese la descripción de la actividad dos')),
                ('actividad_tres', models.TextField(max_length=200, help_text='Ingrese la descripción de la actividad tres')),
                ('actividad_cuatro', models.TextField(max_length=200, help_text='Ingrese la descripción de la actividad cuatro')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['fecha_creacion'],
            },
        ),
    ]
