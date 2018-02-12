# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/10 13:28

# Author: sty

# File: forms.py

from django import forms


class LoginForm(forms.Form):
    """
    登录表单验证
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)