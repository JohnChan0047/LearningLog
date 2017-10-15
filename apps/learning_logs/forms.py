# -*- coding:utf-8 -*- 
__author__ = 'John 2017/10/8 21:31'

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # widgets = {'text': forms.Textarea(attrs={'cols': 120})}