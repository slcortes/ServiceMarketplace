# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_auto_20160405_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': (('can_add_review', 'can_add_review'),)},
        ),
    ]
