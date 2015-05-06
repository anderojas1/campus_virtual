# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0008_auto_20150506_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderteacher',
            name='areaAsignada',
            field=models.CharField(max_length=50),
        ),
    ]
