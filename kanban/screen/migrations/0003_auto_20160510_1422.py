# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_productexecuting_isnew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productexecuting',
            old_name='isnew',
            new_name='new_product',
        ),
    ]