# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0003_auto_20160225_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='summary',
            field=models.CharField(blank=True, default=None, max_length=140, null=True),
        ),
    ]
