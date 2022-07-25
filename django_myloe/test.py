#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-07-22 4:07 PM
# @Author  : myloe
# @File    : test.py
from django.conf import settings
from django.http import JsonResponse
def test(request):
    return JsonResponse({"port": settings.port})