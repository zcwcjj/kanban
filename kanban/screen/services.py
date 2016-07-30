from .models import ProductExecutingDetail


def readProductPlanExcelAndWrite(singleProductionPlan):
    # prepare to open Excel,set style,chose sheet
    import xlwt
    import xlrd
    from xlutils.copy import copy
    from django.utils import timezone
    wb1 = xlrd.open_workbook(
        '/var/www/html/kanban/1.xls', formatting_info=True)
    wb = copy(wb1)
    # wb = xlwt.Workbook()

    style1 = xlwt.Style.easyxf(
        'font: bold off, name SimSun ,height 220; borders:left 1,right 1,top 1,bottom 1; align: wrap on, vert centre, horiz center')
    ws = wb.get_sheet(0)
    plandetails = ProductExecutingDetail.objects.filter(
        productionPlan=singleProductionPlan)
    import io
    ttt = io.BytesIO()
    col = 2
    for plandetail in plandetails:
        ws.write(3, col, str(plandetail.product), style1)
        # ws.write(1, 0, datetime.now())
        if plandetail.isnew:
            ws.write(5, col, str(plandetail.workers), style1)
            ws.write(6, col, str(plandetail.students), style1)
            ws.write(15, col, plandetail.plan, style1)
            ws.write(16, col, plandetail.train_number, style1)
        else:
            ws.write(8, col, str(plandetail.workers), style1)
            ws.write(9, col, str(plandetail.students), style1)
            ws.write(13, col, plandetail, plan, style1)
            ws.write(14, col, plandetail.train_number, style1)

        ws.write(20, col, str(timezone.localtime(
            plandetail.produce_date)), style1)
        col += 1
    wb.save(ttt)
    return ttt
