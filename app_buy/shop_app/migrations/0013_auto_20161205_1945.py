# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(height_field=209, upload_to='', width_field=400),
        ),
    ]
