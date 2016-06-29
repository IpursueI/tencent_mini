# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0016_auto_20160628_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_latitude',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_longitude',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
