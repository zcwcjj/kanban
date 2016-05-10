from django.contrib import admin
from .models import *
from django import forms
# Register your models here.

admin.site.register(AreaStatus)
admin.site.register(Product)



class AreaAdmin(admin.ModelAdmin):
	def process_discipline_tag(self, request):

		return u'<img src="%s" width="200px" height="200px" />' % ( request.process_discipline.url)
	process_discipline_tag.short_description = '工艺纪律检查图片'
	process_discipline_tag.allow_tags = True

	def queryset(self, request, queryset):
		qs = super(AreaAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(id=2)
		print("----------------------")



admin.site.register(Area, AreaAdmin)
admin.site.register(ProductExecuting)