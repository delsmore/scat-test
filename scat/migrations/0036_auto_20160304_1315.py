# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0035_auto_20160304_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]