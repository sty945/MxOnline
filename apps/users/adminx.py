# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/2 21:09

# Author: sty

# File: adminx.py
import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
