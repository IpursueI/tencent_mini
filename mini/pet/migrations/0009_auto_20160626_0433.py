# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0008_auto_20160626_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_picture',
            field=models.BinaryField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.BinaryField(default=0),
        ),
    ]
