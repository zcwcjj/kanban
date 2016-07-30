# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0019_auto_20160627_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productexecutingdetail',
            name='Area',
        ),
        migrations.AddField(
            model_name='productionplan',
            name='Area',
            field=models.ForeignKey(default=1, to='screen.Area', verbose_name='工区'),
            preserve_default=False,
        ),
    ]
