# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0014_auto_20160627_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_latitude',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_longitude',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
