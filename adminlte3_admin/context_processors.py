from django.utils.translation import gettext as _
from django.http import HttpRequest
from django.urls import reverse, NoReverseMatch
from django.contrib.admin.sites import site
from django.apps import apps
from django.utils.text import capfirst


def _build_app_dict(request, label=None):
    """
    Build the app dictionary. The optional `label` parameter filters models
    of a specific app.
    """
    app_dict = {}

    if label:
        models = {
            m: m_a for m, m_a in site._registry.items()
            if m._meta.app_label == label
        }
    else:
        models = site._registry

    for model, model_admin in models.items():
        app_label = model._meta.app_label

        has_module_perms = model_admin.has_module_permission(request)
        if not has_module_perms:
            continue

        perms = model_admin.get_model_perms(request)

        # Check whether user has any perm for this module.
        # If so, add the module to the model_list.
        if True not in perms.values():
            continue

        info = (app_label, model._meta.model_name)
        model_dict = {
            'model': model,
            'name': capfirst(model._meta.verbose_name_plural),
            'icon': model._meta.icon if hasattr(model._meta, 'icon') else 'far fa-circle',
            'object_name': model._meta.object_name,
            'perms': perms,
            'admin_url': None,
            'add_url': None,
        }
        if perms.get('change') or perms.get('view'):
            model_dict['view_only'] = not perms.get('change')
            try:
                model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=site.name)
            except NoReverseMatch:
                pass
        if perms.get('add'):
            try:
                model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=site.name)
            except NoReverseMatch:
                pass

        if app_label in app_dict:
            app_dict[app_label]['models'].append(model_dict)
        else:
            app = apps.get_app_config(app_label)
            app_dict[app_label] = {
                'name': app.verbose_name,
                'icon': app.icon if hasattr(app, 'icon') else 'far fa-circle',
                'app_label': app_label,
                'app_url': reverse(
                    'admin:app_list',
                    kwargs={'app_label': app_label},
                    current_app=site.name,
                ),
                'has_module_perms': has_module_perms,
                'models': [model_dict],
            }

    if label:
        return app_dict.get(label)
    return app_dict


def sidebar_menu(request: HttpRequest) -> dict:
    menu_itens = []
    for app_label, app in _build_app_dict(request).items():
        menu_itens.append(            
            {
                "label": app['name'], 
                "url": app['app_url'], 
                'icon': app['icon'],
                'app': app_label,
                "subitens": [
                    {
                        "label": model['name'], 
                        "url": model['admin_url']
                    } 
                    for model in app['models']
                ]
            }
        )
    return {"layout_sidebar_menu": menu_itens}

