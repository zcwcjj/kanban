# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0015_auto_20160625_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productexecutingdetail',
            options={'verbose_name_plural': '生产计划详情', 'verbose_name': '生产计划详情'},
        ),
    ]
