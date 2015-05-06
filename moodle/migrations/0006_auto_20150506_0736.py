# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0005_auto_20150506_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.CharField(help_text='Ingrese la fecha de nacimiento del usuario', max_length=30),
        ),
    ]
