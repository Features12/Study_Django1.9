# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-23 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
    ]
