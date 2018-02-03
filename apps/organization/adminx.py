# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/3 14:52

# Author: sty

# File: adminx.py
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    """
    城市数据管理
    """
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    """
    课程机构信息管理
    """
    list_display = ['city', 'name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'add_time']
    search_fields = ['city', 'name', 'desc', 'click_num', 'fav_nums', 'image', 'address']
    list_filter = ['city__name', 'name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'add_time']


class TeacherAdmin(object):
    """教师信息管理"""
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

