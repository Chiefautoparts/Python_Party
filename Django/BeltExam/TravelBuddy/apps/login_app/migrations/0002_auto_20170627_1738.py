# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='last_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
    ]
