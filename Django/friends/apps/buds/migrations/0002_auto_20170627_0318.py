# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
