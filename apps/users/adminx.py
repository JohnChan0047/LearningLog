# -*- coding:utf-8 -*- 
__author__ = 'John 2017/10/8 19:20'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

# from .models import UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '博客后台管理系统'
    site_footer = '博客在线'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)