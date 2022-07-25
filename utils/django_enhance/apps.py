#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-07-22 4:28 PM
# @Author  : myloe
# @File    : apps.py

from django.apps import AppConfig as django_app_config
from django.conf import settings

class AppConfig(django_app_config):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kafka'

    def ready(self):
        print("1111")

        # from . import settings as app_settings

        # settings_key = [key for key in dir(app_settings) if not key.startswith("__")]
        # for key in settings_key:
        #     setattr(settings, key, getattr(app_settings, key))
