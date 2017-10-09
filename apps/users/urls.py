# -*- coding:utf-8 -*- 
__author__ = 'John 2017/10/9 13:43'

from django.conf.urls import url

from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]