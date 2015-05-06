# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0007_auto_20150506_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterteacher',
            name='experiencia',
            field=models.PositiveIntegerField(help_text='Ingrese el nombre del Usuario'),
        ),
    ]
