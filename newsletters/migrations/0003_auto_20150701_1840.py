# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20150630_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
