# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0009_auto_20150506_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderteacher',
            old_name='areaAsignada',
            new_name='area_asignada',
        ),
        migrations.AlterField(
            model_name='masterteacher',
            name='experiencia',
            field=models.PositiveIntegerField(),
        ),
    ]
