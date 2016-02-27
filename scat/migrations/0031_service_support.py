# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0030_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='support',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scat.Support'),
        ),
    ]
