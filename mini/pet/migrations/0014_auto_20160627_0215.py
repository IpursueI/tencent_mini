# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0013_auto_20160626_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_token',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='user_token_overdue',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_end_time',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_start_time',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
