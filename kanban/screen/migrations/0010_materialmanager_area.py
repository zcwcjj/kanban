# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0009_auto_20160513_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialmanager',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='screen.Area', verbose_name='所属工区'),
            preserve_default=False,
        ),
    ]
