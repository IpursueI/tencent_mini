# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_auto_20160624_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_pet_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_price',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=2),
        ),
    ]
