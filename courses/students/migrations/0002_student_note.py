# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='note',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]