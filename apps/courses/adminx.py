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


xadmin.site.register(Course, CourseAdmin)