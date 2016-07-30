# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0013_auto_20160625_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductExecutingDetail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('produce_date', models.DateField(verbose_name='计划日期')),
                ('workers', models.CharField(max_length=100)),
                ('students', models.CharField(max_length=100)),
                ('plan', models.IntegerField(verbose_name='计划数量')),
                ('excuted', models.IntegerField(verbose_name='已生产数量')),
                ('isnew', models.BooleanField(verbose_name='是否新造', default=True)),
                ('Area', models.ForeignKey(to='screen.Area', verbose_name='工区')),
                ('product', models.ForeignKey(to='screen.Product', verbose_name='工作内容')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionPlan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('productionPlan_date', models.DateField(verbose_name='计划下达日期')),
            ],
        ),
        migrations.RemoveField(
            model_name='productexecuting',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='productexecuting',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductExecuting',
        ),
        migrations.AddField(
            model_name='productexecutingdetail',
            name='productionPlan',
            field=models.ForeignKey(to='screen.ProductionPlan', verbose_name='计划工单'),
        ),
    ]
