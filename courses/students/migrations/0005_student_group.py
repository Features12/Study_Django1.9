# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-22 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20170322_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Group'),
            preserve_default=False,
        ),
    ]
