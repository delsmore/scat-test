# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0039_service_visible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='visible',
            new_name='published',
        ),
    ]
