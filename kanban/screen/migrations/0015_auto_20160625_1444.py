# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0014_auto_20160625_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WorkCell',
        ),
        migrations.AlterModelOptions(
            name='productionplan',
            options={'verbose_name_plural': '生产计划管理', 'verbose_name': '生产计划管理'},
        ),
    ]
