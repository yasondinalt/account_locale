#! -*- coding: utf-8 -*-

from django.apps import AppConfig

class AccountLocaleAppConfig(AppConfig):
    label = 'account_locale'
    name = 'account_locale'
    verbose_name = 'Account with locale change'

    def ready(self):
        from . import receivers
