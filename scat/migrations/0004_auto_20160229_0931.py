# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0003_auto_20160228_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ManyToManyField(to='scat.Type'),
        ),
    ]
