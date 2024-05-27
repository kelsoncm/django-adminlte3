# -*- coding: utf-8 -*-
from typing import List, Dict, Optional, Any
from django.conf import settings
from django.http import HttpRequest
from django.apps import apps


class MenuItemBadge(object):
    def __init__(self, label: str, color: Optional[str] = None):
        self.label = label
        self.color = color

    def as_html(self):
        return f'<span class="badge {self.color} right">{self.label}</span>'


class MenuItem(object):
    def __init__(
        self,
        label: str,
        url: str,
        icon: Optional[str] = None,
        subitems: Optional[List[Dict[str, Any]]] = None,
        color: Optional[str] = None,
        is_active: Optional[bool] = None,
        badge: Optional[MenuItemBadge] = None,
        **kwargs,
    ):
        self.label = label
        self.url = url
        self.icon = icon if icon is not None else getattr(settings, "DEFAULT_MENU_ICON", "far fa-circle")
        self.subitems = subitems if subitems else []
        self.color = color
        self.is_active = is_active
        self.badge = badge
        self.url = url

    @property
    def badge_as_html(self):
        return self.badge.as_html if self.badge else ""

    def __str__(self):
        return f"{self.label} - {self.url}"


def get_top_menu(request: Optional[HttpRequest] = None) -> List[MenuItem]:
    result = []
    for name, app in apps.app_configs.items():
        if hasattr(app.module, "menus") and hasattr(app.module.menus, "top_menu"):
            result += app.module.menus.top_menu(request)
    return result


def get_sidebar_menu(request: Optional[HttpRequest] = None) -> List[MenuItem]:
    result = []
    for name, app in apps.app_configs.items():
        if hasattr(app.module, "menus") and hasattr(app.module.menus, "sidebar_menu"):
            result += app.module.menus.sidebar_menu(request)
    return result
