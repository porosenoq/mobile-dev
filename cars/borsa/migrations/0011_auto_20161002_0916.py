# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borsa', '0010_car_hp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]