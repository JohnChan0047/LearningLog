from datetime import datetime

from django.db import models

from users.models import UserProfile

# Create your models here.


class Topic(models.Model):

    name = models.CharField(max_length=10, verbose_name='主题')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    user = models.ForeignKey(UserProfile, verbose_name='作者')

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, verbose_name='主题')
    text = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20] + '...'