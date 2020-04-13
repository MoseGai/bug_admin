#!/urs/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterents = [
    url(r'send/sms/',views.send_sms),
    url(r'^register/',views.register,name='register'),# "app01:register"
    
]
