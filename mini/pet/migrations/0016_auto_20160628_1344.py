# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0015_auto_20160627_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_authenticated_picture',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
