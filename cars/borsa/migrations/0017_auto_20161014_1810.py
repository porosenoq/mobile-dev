# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borsa', '0016_auto_20161014_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carphotos',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='images',
            field=models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, to='borsa.CarPhotos'),
            preserve_default=False,
        ),
    ]
