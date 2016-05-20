# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 02:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0008_auto_20160511_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialmanager',
            name='remark',
        ),
        migrations.AddField(
            model_name='materialmanager',
            name='code',
            field=models.CharField(default='hahahah', max_length=60, verbose_name='物料编码'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materialmanager',
            name='isProceed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='materialmanager',
            name='name',
            field=models.CharField(default='hahaha', max_length=60, verbose_name='物料名称'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materialmanager',
            name='publishTime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 13, 2, 39, 9, 60771, tzinfo=utc), verbose_name='发布时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materialmanager',
            name='responsTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='响应时间'),
        ),
        migrations.AlterField(
            model_name='area',
            name='attainment_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='标准工位达标率,单位百分比'),
        ),
        migrations.AlterField(
            model_name='area',
            name='dagerous_map',
            field=models.ImageField(blank=True, upload_to='dagerous_map', verbose_name='工位危险源地图'),
        ),
        migrations.AlterField(
            model_name='area',
            name='exception',
            field=models.ImageField(blank=True, upload_to='exception', verbose_name='当月异常情况'),
        ),
        migrations.AlterField(
            model_name='area',
            name='important_change',
            field=models.ImageField(blank=True, upload_to='important_change', verbose_name='重大更改或整改图片'),
        ),
        migrations.AlterField(
            model_name='area',
            name='improve_proposal',
            field=models.ImageField(blank=True, upload_to='improve_proposal', verbose_name='改善提案图片'),
        ),
        migrations.AlterField(
            model_name='area',
            name='introduce',
            field=models.CharField(blank=True, max_length=1000, verbose_name='介绍,不超过500个字'),
        ),
        migrations.AlterField(
            model_name='area',
            name='managerList',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='管理人员'),
        ),
        migrations.AlterField(
            model_name='area',
            name='organize_framework',
            field=models.ImageField(blank=True, upload_to='organize_framework', verbose_name='工区组织架构图'),
        ),
        migrations.AlterField(
            model_name='area',
            name='pass_rate',
            field=models.ImageField(blank=True, upload_to='pass_rate', verbose_name='当月一次性合格率统计'),
        ),
        migrations.AlterField(
            model_name='area',
            name='process_discipline',
            field=models.ImageField(blank=True, upload_to='process_discipline', verbose_name='工艺纪律检查图片'),
        ),
        migrations.AlterField(
            model_name='area',
            name='process_layout',
            field=models.ImageField(blank=True, upload_to='process_layout', verbose_name='工区工艺布局图'),
        ),
        migrations.AlterField(
            model_name='area',
            name='productlist',
            field=models.ManyToManyField(blank=True, to='screen.Product', verbose_name='能生产的产品列表'),
        ),
        migrations.AlterField(
            model_name='area',
            name='standbook',
            field=models.ImageField(blank=True, upload_to='standbook', verbose_name='工位台账信息'),
        ),
        migrations.AlterField(
            model_name='area',
            name='typical_question',
            field=models.ImageField(blank=True, upload_to='typical_question', verbose_name='典型质量问题'),
        ),
        migrations.AlterField(
            model_name='area',
            name='working_skill',
            field=models.ImageField(blank=True, upload_to='working_skill', verbose_name='班组人员职责以及技能'),
        ),
        migrations.AlterField(
            model_name='area',
            name='working_skill_radar',
            field=models.ImageField(blank=True, upload_to='working_skill_radar', verbose_name='人员技能统计图'),
        ),
    ]
