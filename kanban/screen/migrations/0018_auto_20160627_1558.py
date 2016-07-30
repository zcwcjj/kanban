# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0017_auto_20160627_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productexecutingdetail',
            name='isnew',
            field=models.BooleanField(default=True, verbose_name='新造'),
        ),
    ]
