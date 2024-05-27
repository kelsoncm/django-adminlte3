```python
# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse
from adminlte3.menus import MenuItem


def example_layout_settings(request: HttpRequest) -> dict:
    return {
        "site_title": "AdminLTE 3",
        "layout_home_url_name": "adminlte3:dashboard",
        "layout_register_url_name": "adminlte3:register",
        "layout_term_of_use_url_name": "adminlte3:term_of_use",
        "layout_site_name": "AdminLTE 3",
        "layout_has_navbar_search": True,
        "layout_has_fullscreen_toggler": True,
        "layout_has_customizer": True,
        "layout_has_auth_remembering": True,
        "layout_auto_page_title": request.path.lower()
        .replace("/", " ")
        .lstrip()
        .title(),
    }


def example_user(request: HttpRequest) -> dict:
    short_name = (
        request.user.get_short_name()
        if hasattr(request.user, "get_short_name")
        else "Anônimo"
    )
    return {
        "user_display_name": short_name,
        "user_profile_url": "#",
        "user_profile_thumbnail_url": f"{settings.STATIC_URL}/vendors/adminlte3/img/avatar.png",
    }


def example_top_menu(request: HttpRequest) -> dict:
    return {
        "layout_navbar_menu": [
            MenuItem(_("Início"), reverse("adminlte3:dashboard")),
            MenuItem(_("Admin"), reverse("admin:index")),
        ]
    }


def example_sidebar_menu(request: HttpRequest) -> dict:
    return {
        "layout_sidebar_menu": [
            MenuItem(_("Início"), reverse("adminlte3:dashboard")),
            MenuItem(
                _("Admin"),
                reverse("admin:index"),
                "fas fa-tachometer-alt",
                None,
                [MenuItem(_("User"), reverse("auth:user"))],
            ),
        ]
    }


def example_messages(request: HttpRequest) -> dict:
    return {
        "layout_navbar_message_bar": {
            "count": "+20",
            "see_all_url": "#",
            "messages": [
                {
                    "message_url": "#",
                    "user_thumbnail_url": f"{settings.STATIC_URL}vendors/adminlte3/img/user1-128x128.jpg",
                    "user_name": "Brad Diesel",
                    "text": "Call me whenever you can...",
                    "since": "4 Hours Ago",
                    "star_color": "danger",
                }
            ],
        }
    }


def example_notifications(request: HttpRequest) -> dict:
    return {
        "layout_navbar_notifications_bar": {
            "count": "10",
            "count_label": _("{} notificações").format(215),
            "see_all_url": "#",
            "notification_group": [
                {
                    "url": "#",
                    "label": _("{} novas mensagens").format(204),
                    "since": _("{} mins").format(4),
                    "icon": "fas fa-envelope",
                }
            ],
        }
    }

```
