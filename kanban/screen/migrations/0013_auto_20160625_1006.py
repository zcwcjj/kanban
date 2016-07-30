# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0012_auto_20160513_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCell',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='工作站名称')),
            ],
            options={
                'verbose_name_plural': '生产计划管理',
                'verbose_name': '生产计划管理',
            },
        ),
        migrations.AlterModelOptions(
            name='productexecuting',
            options={},
        ),
        migrations.AlterField(
            model_name='productexecuting',
            name='product',
            field=models.ForeignKey(to='screen.Product', verbose_name='工作内容'),
        ),
    ]
