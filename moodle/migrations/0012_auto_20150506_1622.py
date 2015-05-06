# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0011_auto_20150506_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderteacher',
            options={'ordering': ['area_asignada']},
        ),
        migrations.AlterModelOptions(
            name='masterteacher',
            options={'ordering': ['experiencia']},
        ),
        migrations.AlterModelOptions(
            name='secretariaeducacion',
            options={'ordering': ['codigo']},
        ),
    ]
