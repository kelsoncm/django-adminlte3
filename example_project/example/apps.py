# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.contrib import auth


class ExampleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "example"
    icon = "fa fa-edit"


auth.apps.AuthConfig.icon = "fa fa-user-check"
auth.apps.AuthConfig.verbose_name = "Permissões"
