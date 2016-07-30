from django.contrib import admin
from .models import *
from django import forms
import django.utils.timezone
# Register your models here.

admin.site.register(AreaStatus)
admin.site.register(Product)


class AreaAdmin(admin.ModelAdmin):
    "工区管理"

    def process_discipline_tag(self, request):
        return u'<img src="%s" width="200px" height="200px" />' % (request.process_discipline.url)
    process_discipline_tag.short_description = '工艺纪律检查图片'
    process_discipline_tag.allow_tags = True
    # 确保工长用户只能看到自己的界面

    def get_queryset(self, request):
        qs = super(AreaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            id = request.user.id
            return qs.filter(managerList__id=id)

    filter_horizontal = ('productlist',)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super(AreaAdmin, self).get_fieldsets(request, obj)
        else:
            return [(None, {'fields': (
                    'name', 'statusNow', 'introduce', 'process_discipline',
                    'important_change', 'productlist', 'working_skill',
                    'organize_framework', 'working_skill_radar',
                    'standbook', 'process_layout',
                    'dagerous_map', 'improve_proposal',
                    'attainment_rate', 'pass_rate',
                    'exception', 'typical_question')})]


admin.site.register(Area, AreaAdmin)


class ProductExecutingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'produce_date', 'excuted', 'plan')
    list_editable = ('product', 'produce_date', 'excuted', 'plan')
    ordering = ('-produce_date',)

    def get_queryset(self, request):
        qs = super(ProductExecutingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            id = request.user.id
            return qs.filter(Area__managerList__id=id).filter(produce_date__gte=django.utils.timezone.now().date())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super(ProductExecutingAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'Area':
            kwargs["queryset"] = Area.objects.filter(
                managerList__id=request.user.id)
        elif db_field.name == 'product':
            kwargs["queryset"] = Product.objects.filter(
                area__managerList__id=request.user.id).distinct()
        return super(ProductExecutingAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
# admin.site.register(ProductExecuting, ProductExecutingAdmin)


class ProductExecutingDetailInline(admin.TabularInline):
    model = ProductExecutingDetail
    extra = 3

    def get_querset(self, request):
        qs = super(ProductExecutingDetailInline, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            id = request.user.id
            return qs.filter(Area__managerList__id=id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super(ProductExecutingDetailInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'Area':
            kwargs["queryset"] = Area.objects.filter(
                managerList__id=request.user.id)
        elif db_field.name == 'product':
            kwargs["queryset"] = Product.objects.filter(
                area__managerList__id=request.user.id).distinct()
        return super(ProductExecutingDetailInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ProductionPlanAdmin(admin.ModelAdmin):
    inlines = [
        ProductExecutingDetailInline,
    ]
    actions = ['get_excel']

    def get_excel(modeladmin, request, queryset):
        from django.http import HttpResponse
        from .services import readProductPlanExcelAndWrite
        ttt = readProductPlanExcelAndWrite(queryset[0])
        response = HttpResponse(ttt.getvalue())
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="test.xls"'
        return response
    get_excel.short_description = "下载工作计划"

admin.site.register(ProductionPlan, ProductionPlanAdmin)


class MaterialManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'isProceed', 'publishTime', 'responsTime')
    ordering = ('isProceed',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super(MaterialManagerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'area':
            kwargs['queryset'] = Area.objects.filter(
                managerList__id=request.user.id)
        return super(MaterialManagerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(MaterialManager, MaterialManagerAdmin)
