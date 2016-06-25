# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_auto_20160624_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_introduction',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_title',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participant_user_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_interest',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_latitude',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_longitude',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
