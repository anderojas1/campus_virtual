# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0012_auto_20150506_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderteacher',
            options={'ordering': ['cedula']},
        ),
        migrations.AlterModelOptions(
            name='masterteacher',
            options={'ordering': ['cedula']},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['cedula']},
        ),
    ]
