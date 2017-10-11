from datetime import datetime

from django.db import models

from users.models import UserProfile

# Create your models here.


class Topic(models.Model):

    name = models.CharField(max_length=10, verbose_name='Topic')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add time')
    user = models.ForeignKey(UserProfile, verbose_name='作者')

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, verbose_name='主题')
    text = models.TextField(verbose_name='Entry')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add time')

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20] + '...'