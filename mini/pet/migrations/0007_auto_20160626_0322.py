# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_auto_20160625_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_picture',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_authenticated_picture',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
    ]
