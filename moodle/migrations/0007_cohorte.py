# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0006_auto_20150506_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('slug', models.SlugField(serialize=False, max_length=30, primary_key=True)),
                ('grupo', models.PositiveSmallIntegerField()),
                ('codigo_curso', models.ForeignKey(to='moodle.Curso')),
            ],
        ),
    ]
