# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0050_auto_20160307_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='guid',
            field=models.UUIDField(blank=True, default=None),
        ),
    ]
