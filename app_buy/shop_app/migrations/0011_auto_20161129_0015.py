# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-28 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0010_auto_20161129_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop_cart',
            old_name='number_product',
            new_name='product',
        ),
    ]
