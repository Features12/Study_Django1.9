# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_auto_20161114_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_list',
            name='price',
            field=models.FloatField(),
        ),
    ]
