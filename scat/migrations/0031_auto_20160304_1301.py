# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0030_auto_20160304_1258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='People',
        ),
    ]
