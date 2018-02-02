# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/2 21:09

# Author: sty

# File: adminx.py
import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
