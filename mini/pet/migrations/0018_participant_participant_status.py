# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0017_auto_20160629_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='participant_status',
            field=models.IntegerField(default=0),
        ),
    ]
