# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0021_auto_20160408_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
