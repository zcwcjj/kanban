# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 03:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0010_materialmanager_area'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialmanager',
            options={'verbose_name': '缺料管理', 'verbose_name_plural': '缺料管理'},
        ),
        migrations.RemoveField(
            model_name='materialmanager',
            name='status',
        ),
    ]
