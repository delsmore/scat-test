# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0021_auto_20160226_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
    ]
