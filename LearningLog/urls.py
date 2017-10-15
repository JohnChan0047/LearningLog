"""LearningLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
import xadmin
from apps.learning_logs.upload import upload_image

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 配置主页显示的url
    url(r'', include('learning_logs.urls', namespace='learning_logs')),

    # 用户相关url
    url(r'^user/', include('users.urls', namespace='user')),

    # media配置
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),

    # 配置kindeditor上传
    url(r'^uploads/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]

