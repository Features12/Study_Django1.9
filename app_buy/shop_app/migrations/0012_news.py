# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0011_auto_20161129_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('descriptions', models.TextField()),
            ],
        ),
    ]