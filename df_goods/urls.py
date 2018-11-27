#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from df_goods.views import *


urlpatterns=[
    url(r'^$', index),
    url(r'^list(\d+)_(\d+)_(\d+)/$', goodlist),
    url(r'^(\d+)/$', detail),
]