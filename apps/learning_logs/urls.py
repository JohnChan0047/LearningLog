# -*- coding:utf-8 -*- 
__author__ = 'John 2017/10/8 20:28'


from django.conf.urls import url

from .views import IndexView, TopicView, AddNewTopicView, AddNewEntryView, EditEntryView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^topics/$', TopicsView.as_view(), name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', TopicView.as_view(), name='topic'),
    url(r'^new_topic/$', AddNewTopicView.as_view(), name='new_topic'),
    url(r'^topics/(?P<topic_id>\d+)/new_entry/$', AddNewEntryView.as_view(), name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', EditEntryView.as_view(), name='edit_entry'),
]