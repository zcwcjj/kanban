# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0018_auto_20160627_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionplan',
            name='productionPlan_date',
            field=models.DateField(verbose_name='计划下达日期', editable=False),
        ),
    ]
