# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0014_service_business_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_operations_manager',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='som', to='scat.Person'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so', to='scat.Person'),
        ),
        migrations.AlterField(
            model_name='service',
            name='business_owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bo', to='scat.Person'),
        ),
    ]