# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0027_auto_20160304_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.TextField()),
            ],
            options={
                'ordering': ['hours'],
            },
        ),
    ]
