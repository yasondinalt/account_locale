#! -*- coding: utf-8 -*-

from django.utils.translation import LANGUAGE_SESSION_KEY, check_for_language
from django.contrib.auth.signals import user_logged_in
from account.signals import user_signed_up
from account.signals import updated_account
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_receiver(sender, request, user, **kwargs):
    lang_code = user.account.language
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session[LANGUAGE_SESSION_KEY] = lang_code

@receiver(user_signed_up)
def user_signed_up_receiver(signal, user, form, request, **kwargs):
    if hasattr(request, 'session'):
        lang_code = request.session[LANGUAGE_SESSION_KEY]
        if lang_code and check_for_language(lang_code):
            user.account.language = lang_code
            user.account.save()

@receiver(updated_account)
def updated_account_receiver(signal, user, request, **kwargs):
    lang_code = user.account.language
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session[LANGUAGE_SESSION_KEY] = lang_code

