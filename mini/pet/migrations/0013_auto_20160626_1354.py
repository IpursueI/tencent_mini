# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0012_auto_20160626_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_end_time',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_picture',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_start_time',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
