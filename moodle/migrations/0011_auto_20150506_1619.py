# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0010_auto_20150506_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretariaEducacion',
            fields=[
                ('codigo', models.CharField(serialize=False, primary_key=True, max_length=30)),
                ('entidad_territorial', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('fijo', models.CharField(null=True, max_length=30, blank=True)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(serialize=False, primary_key=True, max_length=30, help_text='Ingrese el numero de Cedula del Usuario'),
        ),
    ]
