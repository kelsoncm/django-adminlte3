# -*- coding: utf-8 -*-
from typing import Union, Dict, List, Any
from django.http import HttpRequest
from django.urls import reverse, NoReverseMatch
from django.contrib.admin.sites import site
from django.apps import apps
from django.utils.text import capfirst


def safe_reverse(has_permission: bool, to_reverse: str) -> Union[str, None]:
    if not has_permission:
        return None
    try:
        return reverse(to_reverse)
    except NoReverseMatch:
        return None


def _build_app_dict(request, label=None) -> Dict[str, Dict[str, Any]]:
    """
    Build the app dictionary. The optional `label` parameter filters models
    of a specific app.
    """
    app_dict = {}

    models = {m: m_a for m, m_a in site._registry.items() if m._meta.app_label == label} if label else site._registry

    for model, model_admin in models.items():
        app_label = model._meta.app_label

        if app_label not in app_dict:
            app = apps.get_app_config(app_label)
            app_dict[app_label] = {
                "name": app.verbose_name,
                "icon": getattr(app, "icon", "far fa-circle"),
                "app_label": app_label,
                "app_url": reverse("admin:app_list", None, [], {"app_label": app_label}, site.name),
                "has_module_perms": model_admin.has_module_permission(request),
                "view_only": False,
                "models": [],
            }

        info = (app_label, model._meta.model_name)
        perms = model_admin.get_model_perms(request)
        can_view = perms.get("change") or perms.get("view")
        can_add = perms.get("add")

        app_dict[app_label]["models"].append(
            {
                "model": model,
                "name": capfirst(model._meta.verbose_name_plural),
                "icon": getattr(model._meta, "icon", "far fa-circle"),
                "object_name": model._meta.object_name,
                "perms": perms,
                "admin_url": safe_reverse(can_view, "admin:%s_%s_changelist" % info),
                "add_url": safe_reverse(can_add, "admin:%s_%s_add" % info),
            }
        )

    return app_dict.get(label) if label else app_dict


def sidebar_menu(request: HttpRequest) -> Dict[str, List[Dict[str, Any]]]:
    menu_itens = []
    for app_label, app in _build_app_dict(request).items():
        menu_itens.append(
            {
                "label": app["name"],
                "url": app["app_url"],
                "icon": app.get("icon", "far fa-circle"),
                "app": app_label,
                "subitens": [
                    {"label": model["name"], "url": model["admin_url"], "icon": model.get("icon", "far fa-circle")}
                    for model in app["models"]
                ],
            }
        )
    return {"layout_sidebar_menu": menu_itens}
