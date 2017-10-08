# -*- coding:utf-8 -*- 
__author__ = 'John 2017/10/8 20:09'

import xadmin
from xadmin import views

from .models import Topic, Entry


class TopicAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']


class EntryAdmin(object):
    list_display = ['topic', 'text', 'add_time']
    search_fields = ['topic', 'text', 'add_time']
    list_filter = ['topic__name', 'text', 'add_time']


xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Entry, EntryAdmin)