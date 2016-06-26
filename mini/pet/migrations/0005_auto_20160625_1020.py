# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_auto_20160625_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_end_time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_start_time',
            field=models.DateField(null=True),
        ),
    ]
