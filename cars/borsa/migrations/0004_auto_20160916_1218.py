# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borsa', '0003_auto_20160916_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='condition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='borsa.Condition'),
            preserve_default=False,
        ),
    ]
