# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0051_auto_20160307_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='guid',
            field=models.UUIDField(blank=True, default=None, null=True),
        ),
    ]
