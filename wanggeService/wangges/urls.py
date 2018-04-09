# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : urls.py
Description :
@Author :       pchaos
date：          18-4-3
-------------------------------------------------
Change Activity:
               18-4-3:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



app_name="wangges"

urlpatterns = [
    url(r'^wangges/stocks/$', views.stockcode_list, name='stockcodeList'),
    url(r'^wangges/stocks/(?P<pk>[0-9]+)$', views.stockcode_detail, name='stockcodeDetail'),
    url(r'^ZXG/$', views.ZXG_list, name='ZXGList'),
    url(r'^ZXG/(?P<pk>[0-9]+)$', views.ZXG_detail, name='ZXGDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)