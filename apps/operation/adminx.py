# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/3 15:16

# Author: sty

# File: adminx.py
import xadmin

from .models import UserMessage, UserAsk, UserCourse, UserFavorite, CourseComments


class UserMessageAdmin(object):
    """
    用户消息管理
    """
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserAskAdmin(object):
    """
    用户咨询管理
    """
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserCourseAdmin(object):
    """
    用户课程管理
    """
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course',]
    list_filter = ['user', 'course', 'add_time']


class UserFavoriteAdmin(object):
    """
    用户收藏管理
    """
    list_display = ['user', 'fac_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fac_id', 'fav_type']
    list_filter = ['user', 'fac_id', 'fav_type', 'add_time']


class CourseCommentsAdmin(object):
    """
    课程评论管理
    """
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)