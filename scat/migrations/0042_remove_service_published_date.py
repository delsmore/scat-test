# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0041_auto_20160305_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='published_date',
        ),
    ]