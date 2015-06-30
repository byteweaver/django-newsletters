# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name_plural': 'Subscriptions', 'verbose_name': 'Subscription'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 30, 0, 9, 7, 520649, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='ip',
            field=models.IPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
    ]
