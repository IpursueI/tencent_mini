# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_title', models.CharField(max_length=30)),
                ('activity_introduction', models.CharField(max_length=300)),
                ('activity_picture', models.ImageField(upload_to=b'')),
                ('activity_start_time', models.TimeField()),
                ('activity_end_time', models.TimeField()),
                ('activity_status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('participant_user_type', models.BooleanField()),
                ('participant_activity_id', models.ForeignKey(to='pet.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('user_password', models.CharField(max_length=100)),
                ('user_gender', models.BooleanField()),
                ('user_age', models.IntegerField()),
                ('user_address', models.CharField(max_length=200)),
                ('user_avatar', models.ImageField(upload_to=b'')),
                ('user_nickname', models.CharField(max_length=20)),
                ('user_longitude', models.DecimalField(max_digits=6, decimal_places=3)),
                ('user_latitude', models.DecimalField(max_digits=6, decimal_places=3)),
                ('user_interest', models.IntegerField()),
                ('user_authenticated', models.BooleanField()),
                ('user_authenticated_picture', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='participant_user_id',
            field=models.ForeignKey(to='pet.User'),
        ),
    ]
