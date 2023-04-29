# -*- coding: utf-8 -*-
from django.http import HttpRequest
from django.urls import reverse, NoReverseMatch
from django.contrib.admin.sites import site
from django.apps import apps
from django.utils.text import capfirst


def __add_to_model_dict(model_dict: dict, key: str, check: bool, to_reverse: str, current_app: str):
    if check:
        try:
            model_dict[key] = reverse(to_reverse, current_app)
        except NoReverseMatch:
            pass


def _build_app_dict(request, label=None):
    """
    Build the app dictionary. The optional `label` parameter filters models
    of a specific app.
    """
    app_dict = {}

    models = {m: m_a for m, m_a in site._registry.items() if m._meta.app_label == label} if label else site._registry

    for model, model_admin in models.items():
        app_label = model._meta.app_label
        info = (app_label, model._meta.model_name)

        has_module_perms = model_admin.has_module_permission(request)
        perms = model_admin.get_model_perms(request)
        can_view = perms.get("change") or perms.get("view")
        can_change = perms.get("change")
        can_add = perms.get("add")

        icon = model._meta.icon if hasattr(model._meta, "icon") else "far fa-circle"

        if not has_module_perms or True not in perms.values():
            continue

        model_dict = {
            "model": model,
            "name": capfirst(model._meta.verbose_name_plural),
            "icon": icon,
            "object_name": model._meta.object_name,
            "perms": perms,
        }

        __add_to_model_dict(model_dict, "admin_url", can_view, "admin:%s_%s_changelist" % info, site.name)
        __add_to_model_dict(model_dict, "add_url", can_add, "admin:%s_%s_add" % info, site.name)

        if app_label in app_dict:
            app_dict[app_label]["models"].append(model_dict)

        app = apps.get_app_config(app_label)
        app_dict[app_label] = {
            "name": app.verbose_name,
            "icon": icon,
            "app_label": app_label,
            "app_url": reverse("admin:app_list", None, [], {"app_label": app_label}, site.name),
            "has_module_perms": has_module_perms,
            "view_only": can_view and not can_change,
            "models": [model_dict],
        }

    return app_dict.get(label) if label else app_dict


def sidebar_menu(request: HttpRequest) -> dict:
    menu_itens = []
    for app_label, app in _build_app_dict(request).items():
        menu_itens.append(
            {
                "label": app["name"],
                "url": app["app_url"],
                "icon": app["icon"],
                "app": app_label,
                "subitens": [{"label": model["name"], "url": model["admin_url"]} for model in app["models"]],
            }
        )
    return {"layout_sidebar_menu": menu_itens}
