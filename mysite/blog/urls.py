from django.conf.urls import include, url
from django.contrib import admin
from .views import view1

urlpatterns = [
    url(r'^$', view1),
]