# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_service_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='is_active',
            new_name='is_open',
        ),
    ]
