from django.db import models
from django.contrib.auth.models import AbstractUser

from _datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    birthday = models.DateField(verbose_name='生日', null=True)
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name='头像')
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username