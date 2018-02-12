# !/usr/bin/env python

# -*- coding: utf-8 -*-

# Time: 2018/2/10 13:28

# Author: sty

# File: forms.py

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    登录表单验证
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    """
    注册表单的验证
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 应用验证码
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


