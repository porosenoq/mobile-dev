# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 14:01
from __future__ import unicode_literals

import borsa.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borsa', '0012_auto_20161014_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=borsa.models.photos_papka)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='photos',
        ),
        migrations.AddField(
            model_name='carphotos',
            name='carid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borsa.Car'),
        ),
    ]
