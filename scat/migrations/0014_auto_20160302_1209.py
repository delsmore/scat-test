# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0013_auto_20160302_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b'/images/people'),
        ),
    ]
