from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect
from .models import  *
from django.template import Context, Template, loader
from django.conf import settings
from django.utils import timezone

# Create your views here.

# 只用来修饰view函数的第一个参数
# 如果没有设定区域，导航到选择区域位置
def localtionSettedOrRedirect(f):
	def func(*args, **kwargs):
		
		try:
			req = args[0].COOKIES["areaid"]
			if len(Area.objects.filter(id=req)) != 1:
				raise Exception("notfounded")
			
			return f(*args, **kwargs)

		except Exception as e:
			return HttpResponseRedirect("http://10.19.6.75:8000/screen/index")
	return func

#
def ajax_get_data(request):
	json_data = Area.objects.all()[0].important_change.url
	return HttpResponse('%s({"name":"%s"})' % (request.GET["callback"], json_data), content_type="application/json")

# 接受?page=xxx的方法
@localtionSettedOrRedirect
def get_page(request,page):
	if page != None:
		templateList=['frame.html','kanban01.html', 'kanban02.html', 'kanban03.html', 'kanban4.html', 'kanban5.html', \
		'kanban6.html', 'kanban7.html', 'kanban8.html', 'kanban9.html']
		
		try:
			pageIndex = int(page)
			areaid = request.COOKIES["areaid"]
			temp = loader.get_template(templateList[pageIndex])
			model = Area.objects.filter(id=areaid)[0]
			planList = ProductExecuting.objects.filter(Area__id=areaid).filter(produce_date=timezone.now())

		except Exception as e:
			# should return 404
			print("--------",e)
			pass
		else:
			context = {'STATIC_URL': settings.STATIC_URL,'model': model, 'planList': planList}
			
		finally:
			return HttpResponse(temp.render(context))


def choose_area(request):
	temp = loader.get_template('area.html')
	areas = Area.objects.all()
	context = {"arealist":areas, 'STATIC_URL': settings.STATIC_URL}
	httpR = HttpResponse(temp.render(context))
	httpR.set_cookie("areaid", "1", 100000)
	return httpR
	
def welcome(request):
	temp = loader.get_template('welcome.html')
	areas = Area.objects.all()
	context = {"arealist":areas, 'STATIC_URL': settings.STATIC_URL}
	httpR = HttpResponse(temp.render(context))
	# httpR.set_cookie("areaid", "1", 100000)
	return httpR