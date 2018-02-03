# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/3 10:13

# Author: sty

# File: adminx.py

from .models import Course, Lesson, Video, CourseResources

import xadmin


class CourseAdmin(object):
    """
    课程的管理
    """
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']


class LessonAdmin(object):
    """
    章节的管理
    """
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    """
    视频的管理
    """
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourcesAdmin(object):
    """
    课程资源的管理
    """
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResources, CourseResourcesAdmin)
