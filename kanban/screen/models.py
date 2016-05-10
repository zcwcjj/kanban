from django.db import models
from django.conf import settings
# Create your models here.
# 工位状态
class AreaStatus(models.Model):
	state = models.CharField('产品状态', max_length=30)
	def __str__(self):
		return self.state

# 产品介绍
class Product(models.Model):
	name = models.CharField("产品名称", max_length=100)
	pic = models.ImageField(upload_to='product_pic', verbose_name='介绍图片')
	def __str__(self):
		return self.name

class ProductExecuting(models.Model):
	produce_date = models.DateField("计划日期")
	Area = models.ForeignKey('Area', verbose_name='工区')
	# 此处是否需要额外添加Area
	product = models.ForeignKey('Product', verbose_name='产品')
	plan = models.IntegerField('计划数量',)
	excuted = models.IntegerField('已生产数量')
	isnew = models.BooleanField("是否新造", default=True)

	def __str__(self):
		return self.product.name +"\t"+ str(self.produce_date)


class EquipmentManager(models.Model):
	status = models.CharField('状态', max_length=30)
	validity_date = models.DateField('有效期')
	Area = models.ForeignKey('Area', verbose_name='所在工区')
	equipment_check = models.ImageField('设备点检', upload_to='equipment_check')

class MaterialManager(models.Model):
	status = models.CharField('状态', max_length=30)
	remark =models.CharField('缺料统计', max_length=400)





class Area(models.Model):
	# general 
	avaliable = models.BooleanField("是否启用")
	name = models.CharField('工区名称,必须唯一', max_length=50, unique=True)
	statusNow = models.ForeignKey(AreaStatus, verbose_name='当前状态')
	# page1 工区简介
	introduce = models.CharField(max_length=1000, verbose_name='介绍,不超过500个字')
	process_discipline = models.ImageField('工艺纪律检查图片', upload_to='process_discipline')
	# security_cross
	important_change = models.ImageField('重大更改或整改图片', upload_to='important_change')

	#page2 工区域的产品
	productlist = models.ManyToManyField(Product, verbose_name='能生产的产品列表')

	#page4 人员组织和技能
	working_skill = models.ImageField('班组人员职责以及技能', upload_to='working_skill')
	organize_framework = models.ImageField('工区组织架构图', upload_to='organize_framework')
	working_skill_radar = models.ImageField('人员技能统计图' , upload_to='working_skill_radar')

	#page5 
	standbook = models.ImageField('工位台账信息', upload_to='standbook')

	#page6
	process_layout = models.ImageField('工区工艺布局图', upload_to='process_layout')

	#page7
	dagerous_map = models.ImageField('工位危险源地图', upload_to='dagerous_map')

	#page8
	improve_proposal = models.ImageField('改善提案图片', upload_to='improve_proposal')
	attainment_rate = models.DecimalField('标准工位达标率,单位百分比', max_digits=4, decimal_places=2)

	#page9
	pass_rate = models.ImageField('当月一次性合格率统计', upload_to='pass_rate')
	exception = models.ImageField('当月异常情况', upload_to='exception')
	typical_question = models.ImageField('典型质量问题', upload_to='typical_question')

	def __str__(self):
		return self.name



	




