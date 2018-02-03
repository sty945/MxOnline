# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/2 21:09

# Author: sty

# File: adminx.py
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    """
    # 创建Xadmin的全局管理器并与view绑定。
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    # 将左侧菜单栏收起来
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    """
    将邮箱验证信息添加到xadmin中来
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    """
    添加轮播图信息到xadmin中来
    """
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将头部与脚部信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)
