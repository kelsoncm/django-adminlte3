# -*- coding: utf-8 -*-
from typing import Union, Dict, List, Any
from django.http import HttpRequest
from django.urls import reverse, NoReverseMatch
from django.contrib.admin.sites import site
from django.apps import apps
from django.utils.text import capfirst
from adminlte3.menus import MenuItem


def _safe_reverse(has_permission: bool, to_reverse: str) -> str | None:
    if not has_permission:
        return None
    try:
        return reverse(to_reverse)
    except NoReverseMatch:
        return None


def admin_menus(request: HttpRequest) -> list[MenuItem]:
    """
    Build the app dictionary. The optional `label` parameter filters models
    of a specific app.
    """
    app_dict = {}

    # models = {m: m_a for m, m_a in site._registry.items() if m._meta.app_label == label} if label else site._registry
    models = site._registry

    for model, model_admin in models.items():
        meta = model._meta
        app_label = meta.app_label

        if app_label not in app_dict:
            app = apps.get_app_config(app_label)
            app_dict[app_label] = MenuItem(
                app.verbose_name,
                reverse("admin:app_list", None, [], {"app_label": app_label}, site.name),
                getattr(app, "icon", None),
                [],
                has_module_perms=model_admin.has_module_permission(request),
            )

        app_menu_item = app_dict[app_label]
        info = (app_label, meta.model_name)
        perms = model_admin.get_model_perms(request)
        can_view = perms.get("change") or perms.get("view")
        can_add = perms.get("add")

        app_menu_item.subitems.append(
            MenuItem(
                capfirst(model._meta.verbose_name_plural),
                _safe_reverse(can_view, "admin:%s_%s_changelist" % info),
                getattr(meta, "icon", None),
                model=model,
                object_name=meta.object_name,
                perms=perms,
                add_url=_safe_reverse(can_add, "admin:%s_%s_add" % info),
            )
        )

    return list(app_dict.values())


def sidebar_menu(request: HttpRequest) -> dict:
    return {"layout_sidebar_menu": admin_menus(request)}


def top_menu(request: HttpRequest) -> dict:
    return sidebar_menu(request)
