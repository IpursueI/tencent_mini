# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_auto_20160625_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='participant_activity_id',
            new_name='participant_activity',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='participant_user_id',
            new_name='participant_user',
        ),
    ]
