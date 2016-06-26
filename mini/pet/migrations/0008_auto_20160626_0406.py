# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0007_auto_20160626_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_price',
            field=models.IntegerField(default=0),
        ),
    ]
