# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0009_auto_20160626_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_picture',
            field=models.BinaryField(default=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.BinaryField(default=b''),
        ),
    ]
