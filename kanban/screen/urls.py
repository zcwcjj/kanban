from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.ajax_get_data),
    url(r'^page/([0-9]{1})/$', views.get_page),
    url(r'^index', views.choose_area),
    url(r'^status', views.getstatus),
    url(r'^refresh', views.getRefresh),
    url(r'^test/id/([0-9])', views.test),
    
    

]