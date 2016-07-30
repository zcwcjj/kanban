from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import Context, Template, loader
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.detail import SingleObjectMixin
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
            print("------------------", e)
            return HttpResponseRedirect("/screen/index")
    return func

#


def ajax_get_data(request):
    json_data = Area.objects.all()[0].important_change.url
    return HttpResponse(
        '%s({"name":"%s"})' % (request.GET["callback"],
                               json_data), content_type="application/json")

# 接受?page=xxx的方法


@localtionSettedOrRedirect
def get_page(request, page):
    if page is not None:
        templateList = [
            'frame.html', 'kanban01.html', 'kanban02.html', 'kanban03.html',
            'kanban04.html', 'kanban05.html',
            'kanban06.html', 'kanban07.html', 'kanban08.html', 'kanban09.html']

        try:
            pageIndex = int(page)
            areaid = request.COOKIES["areaid"]
            temp = loader.get_template(templateList[pageIndex])
            model = Area.objects.filter(id=areaid).filter(avaliable=True)
            if len(model) > 0:
                model = model[0]
            else:
                model = None
            materialerror = False
            planList = ProductExecutingDetail.objects.filter(
                productionPlan__Area__id=areaid).filter(
                Q(produce_date__year=timezone.now().year) &
                Q(produce_date__month=timezone.now().month) &
                Q(produce_date__day=timezone.now().day))
            if pageIndex == 5:
                materialManager = MaterialManager.objects.filter(
                    area__id=areaid).filter(
                    Q(publishTime__gt=timezone.now().date()) |
                    Q(isProceed=False)
                ).order_by('isProceed')
                if len(MaterialManager.objects.filter(
                    area__id=areaid).filter(isProceed=False)
                ) > 0:
                    materialerror = True
            else:
                materialManager = None

        except Exception as e:
            # should return 404
            print("--------", e)
            pass
        else:
            context = {
                'STATIC_URL': settings.STATIC_URL,
                'model': model, 'planList': planList,
                'material': materialManager,
                'materialerror': materialerror}

        finally:
            return HttpResponse(temp.render(context))


def choose_area(request):
    temp = loader.get_template('SelectWorkspace.html')
    areas = Area.objects.all().filter(avaliable=True)
    context = {"arealist": areas, 'STATIC_URL': settings.STATIC_URL}
    httpR = HttpResponse(temp.render(context))
    # httpR.set_cookie("areaid", "1", 100000)
    return httpR


@login_required
def test1(request, id):
    temp = loader.get_template('area.html')
    areas = Area.objects.all().filter(avaliable=True)
    area_1 = Area.objects.all().filter(id=id)[0]
    if request.method == 'GET':

        form = TestForm(instance=area_1)
        context = {"arealist": areas,
                   'STATIC_URL': settings.STATIC_URL, 'form': form}
        # httpR = HttpResponse(temp.render(context))
        # httpR.set_cookie("areaid", "1", 100000)
        return render(request, 'area.html', context)

    elif request.method == 'POST':
        x = TestForm(request.POST, instance=area_1)
        x.save()
        return HttpResponseRedirect('/screen/test/id/{0}'.format(id))


def test(request, id):
    # temp = loader.get_template('area.html')
    areas = Area.objects.all().filter(avaliable=True)
    area_1 = Area.objects.all().filter(id=id)[0]
    if request.method == 'GET':
        import xlwt
        import xlrd
        from xlutils.copy import copy
        from .services import readProductPlanExcelAndWrite
        ttt = readProductPlanExcelAndWrite(ProductionPlan.objects.all()[0])
        response = HttpResponse(ttt.getvalue())
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="test.xls"'
        return response
    elif request.method == 'POST':
        x = TestForm(request.POST, instance=area_1)
        x.save()
        return HttpResponseRedirect('/screen/test/id/{0}'.format(id))


def getstatus(request):
    areaid = request.COOKIES["areaid"]
    funcname = request.GET["callback"]
    model = Area.objects.filter(id=areaid).filter(avaliable=True)
    if len(model) > 0:
        model = model[0]
    else:
        model = None

    httpR = HttpResponse("%s(\"%s\")" % (funcname, str(model.statusNow)))
    # httpR.set_cookie("areaid", "1", 100000)
    return httpR

from django.core.signals import request_finished
from django.dispatch import receiver
@receiver(request_finished)
def mycallback(sender, **kwargs):
    print("---------------------request finished!")


def getRefresh(request):
    areaid = request.COOKIES["areaid"]
    funcname = request.GET["callback"]
    model = Area.objects.filter(id=areaid).filter(avaliable=True)
    if len(model) > 0:
        model = model[0]
    from  django.utils import timezone
    tz = timezone.get_current_timezone()
    timestamp = tz.normalize(model.update_time)

    if areaid == '1':
        httpR = HttpResponse("%s({\"ref\":1,\"timestamp\":\"%s\",\"list\":%s})" % (funcname, timestamp, [3,4]))
    else:
        httpR = HttpResponse("%s({\"ref\":0,\"timestamp\":\"%s\",\"list\":%s})" % (funcname, timestamp, [1,2,3,4,5,6,7,8,9]))
    return httpR