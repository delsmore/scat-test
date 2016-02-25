# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0002_auto_20160225_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='summary',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
