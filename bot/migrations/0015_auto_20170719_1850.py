# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-07-19 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20170719_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipolygon',
            name='name',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
    ]
