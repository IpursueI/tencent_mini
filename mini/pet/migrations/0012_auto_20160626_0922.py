# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0011_auto_20160626_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_picture',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.ImageField(upload_to=b''),
        ),
    ]
