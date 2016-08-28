# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 10:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default=datetime.datetime(2016, 8, 28, 10, 51, 32, 388204, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(choices=[('1', 'POLAND'), ('2', 'USA'), ('3', 'GERMANY'), ('4', 'FRANCE')], default='POLAND', max_length=9),
        ),
    ]
