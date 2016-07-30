# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0016_auto_20160627_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_time',
            field=models.IntegerField(verbose_name='新造工时', default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='repair_time',
            field=models.IntegerField(verbose_name='检修工时', default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productexecutingdetail',
            name='train_number',
            field=models.CharField(verbose_name='生产列数', blank=True, null=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='productexecutingdetail',
            name='produce_date',
            field=models.DateTimeField(verbose_name='计划日期'),
        ),
        migrations.AlterField(
            model_name='productexecutingdetail',
            name='students',
            field=models.CharField(verbose_name='学员', max_length=100),
        ),
        migrations.AlterField(
            model_name='productexecutingdetail',
            name='workers',
            field=models.CharField(verbose_name='操作者', max_length=100),
        ),
    ]
