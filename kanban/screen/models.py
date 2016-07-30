from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
# 工位状态


class AreaStatus(models.Model):
    state = models.CharField('产品状态', max_length=30)

    def __str__(self):
        return self.state

    class Meta:
        verbose_name = "工区状态管理"
        verbose_name_plural = "工区状态管理"

# 产品，包括半成品


class Product(models.Model):
    name = models.CharField("产品名称", max_length=100)
    pic = models.ImageField(upload_to='product_pic', verbose_name='介绍图片')
    new_time = models.IntegerField('新造工时')
    repair_time = models.IntegerField('检修工时')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品管理"
        verbose_name_plural = "产品管理"


class ProductionPlan(models.Model):
    productionPlan_date = models.DateField(
        "计划下达日期")
    Area = models.ForeignKey('Area', verbose_name='工区')

    def __str__(self):
        return self.Area.name + " " + str(self.productionPlan_date)

    class Meta:
        verbose_name = '生产计划管理'
        verbose_name_plural = "生产计划管理"


class ProductExecutingDetail(models.Model):
    produce_date = models.DateTimeField("计划日期")
    product = models.ForeignKey('Product', verbose_name='工作内容')
    workers = models.CharField("操作者", max_length=100)
    students = models.CharField('学员', max_length=100)
    plan = models.IntegerField('计划数量',)
    excuted = models.IntegerField('已生产数量')
    isnew = models.BooleanField("新造", default=True)
    productionPlan = models.ForeignKey('ProductionPlan', verbose_name='计划工单')
    train_number = models.CharField(
        '生产列数', max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = '生产计划详情'
        verbose_name_plural = '生产计划详情'

    def finished(self):
        return (self.plan == self.excuted)

    def __str__(self):
        return "生产计划：" + str(self.produce_date)


class WorkCell(models.Model):
    name = models.CharField("工作站名称", max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.product.name + "\t" + str(self.produce_date)


class EquipmentManager(models.Model):
    status = models.CharField('状态', max_length=30)
    validity_date = models.DateField('有效期')
    Area = models.ForeignKey('Area', verbose_name='所在工区')
    equipment_check = models.ImageField('设备点检', upload_to='equipment_check')


class MaterialManager(models.Model):
    isProceed = models.BooleanField('已响应', default=False)
    code = models.CharField('物料编码', max_length=60)
    name = models.CharField('物料名称', max_length=60)
    publishTime = models.DateTimeField('发布时间')
    responsTime = models.DateTimeField('响应时间', null=True, blank=True)
    area = models.ForeignKey('Area', verbose_name='所属工区')

    class Meta:
        verbose_name = '缺料管理'
        verbose_name_plural = '缺料管理'


class Area(models.Model):
    "工区管理"
    # general
    managerList = models.ManyToManyField(
        User, verbose_name="管理人员", null=True, blank=True)
    avaliable = models.BooleanField("是否启用", default=False)
    name = models.CharField('工区名称,必须唯一', max_length=50, unique=True)
    statusNow = models.ForeignKey(AreaStatus, verbose_name='当前状态')
    # page1 工区简介
    introduce = models.CharField(
        max_length=1000, verbose_name='介绍,不超过500个字', blank=True)
    process_discipline = models.ImageField(
        '工艺纪律检查图片', upload_to='process_discipline', blank=True)
    # security_cross
    important_change = models.ImageField(
        '重大更改或整改图片', upload_to='important_change', blank=True)

    # page2 工区域的产品
    productlist = models.ManyToManyField(
        Product, verbose_name='能生产的产品列表', blank=True)

    # page4 人员组织和技能
    working_skill = models.ImageField(
        '班组人员职责以及技能', upload_to='working_skill', blank=True)
    organize_framework = models.ImageField(
        '工区组织架构图', upload_to='organize_framework', blank=True)
    working_skill_radar = models.ImageField(
        '人员技能统计图', upload_to='working_skill_radar', blank=True)

    # page5
    standbook = models.ImageField('工位台账信息', upload_to='standbook', blank=True)

    # page6
    process_layout = models.ImageField(
        '工区工艺布局图', upload_to='process_layout', blank=True)

    # page7
    dagerous_map = models.ImageField(
        '工位危险源地图', upload_to='dagerous_map', blank=True)

    # page8
    improve_proposal = models.ImageField(
        '改善提案图片', upload_to='improve_proposal', blank=True)
    attainment_rate = models.DecimalField(
        '标准工位达标率,单位百分比', max_digits=4, decimal_places=2, blank=True)

    # page9
    pass_rate = models.ImageField(
        '当月一次性合格率统计', upload_to='pass_rate', blank=True)
    exception = models.ImageField('当月异常情况', upload_to='exception', blank=True)
    typical_question = models.ImageField(
        '典型质量问题', upload_to='typical_question', blank=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工区管理"
        verbose_name_plural = "工区管理"
