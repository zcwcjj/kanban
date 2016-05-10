# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 06:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0005_remove_productexecuting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productexecuting',
            name='isnew',
            field=models.BooleanField(default=True, verbose_name='是否新造'),
        ),
        migrations.AddField(
            model_name='productexecuting',
            name='produce_date',
            field=models.DateField(default=datetime.datetime(2016, 5, 10, 6, 25, 42, 36732, tzinfo=utc), unique_for_date=True, verbose_name='计划日期'),
            preserve_default=False,
        ),
    ]
