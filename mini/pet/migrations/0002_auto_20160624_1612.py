# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_introduction',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_picture',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participant_user_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_authenticated_picture',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_interest',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_latitude',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_longitude',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
