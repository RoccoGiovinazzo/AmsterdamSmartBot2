# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-07-19 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_multipolygon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multipolygon',
            name='id',
        ),
        migrations.AlterField(
            model_name='multipolygon',
            name='name',
            field=models.CharField(default=' ', max_length=250, primary_key=True, serialize=False),
        ),
    ]
