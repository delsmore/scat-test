# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0033_auto_20160304_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'ordering': ['hours'], 'verbose_name_plural': 'availability'},
        ),
    ]
