# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import PAGE_VAR
from django.template.defaultfilters import register
from django.forms.fields import Field
from django.utils.safestring import SafeString


@register.filter(is_safe=False)
# @stringfilter
def quiet(field: Field):
    return ""


@register.simple_tag
def render_sidebarmenu_list(menu_items: list, top_level=True) -> SafeString:

    def __concatenate(check: bool, value: str, otherwise: str = ""):
        return value if check else otherwise

    if len(menu_items) == 0:
        return mark_safe("")
    result = __concatenate(not top_level, '<ul class="nav nav-treeview">')
    for mi in menu_items:
        result += __concatenate(
            mi.url, '<li class="nav-item">', '<li class="nav-header">'
        )
        result += __concatenate(
            mi.url is not None, f'<a href="{mi.url}" class="nav-link {mi.is_active}">'
        )
        result += f'<i class="nav-icon {mi.icon} {mi.color}"></i>'
        result += "<p>"
        result += mi.label
        result += mi.badge_as_html
        result += __concatenate(
            len(mi.subitems) > 0, '<i class="right fas fa-angle-left"></i>'
        )
        result += "</p>"
        result += __concatenate(mi.url is not None, "</a>")
        result += __concatenate(
            len(mi.subitems) > 0, render_sidebarmenu_list(mi.subitems, False)
        )
        result += "</li>"
    result += __concatenate(not top_level, "</ul>")
    return mark_safe(result)


@register.simple_tag
def render_topmenu_list(menu_items: list, top_level=True) -> SafeString:

    SUBITEMS_EXTRA = 'role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"'
    A_TOP_WITH_SUBITEMS = f'class="nav-link dropdown-toggle" {SUBITEMS_EXTRA}'
    A_TOP_WITHOUT_SUBITEMS = f'class="nav-link"'
    A_NONTOP_WITH_SUBITEMS = f'class="dropdown-item dropdown-toggle" {SUBITEMS_EXTRA}'
    A_NONTOP_WITHOUT_SUBITEMS = f'class="dropdown-item"'

    if len(menu_items) == 0:
        return mark_safe("")

    def _build(items, top):
        result = ""
        for mi in items:
            subitems = len(mi.subitems) > 0
            if top:
                li_attrs = f""" class="nav-item {'dropdown' if subitems else ''}" """
                a_attrs = f""" {A_TOP_WITH_SUBITEMS if subitems else A_TOP_WITHOUT_SUBITEMS} """
            else:
                li_attrs = ' class="dropdown-submenu dropdown-hover"'
                a_attrs = f""" {A_NONTOP_WITH_SUBITEMS if subitems else A_NONTOP_WITHOUT_SUBITEMS} """
            subs = _build(mi.subitems, False)
            subs = f'<ul class="dropdown-menu border-0 shadow">{subs}</ul>'
            label = f'<i class="nav-icon {mi.icon} {mi.color}"></i> {mi.label}{mi.badge_as_html}'
            result += f"""<li {li_attrs}><a {a_attrs} href="#">{label}</a>{subs}</li>"""

        return result

    return mark_safe(_build(menu_items, top_level))


@register.simple_tag
def page_item(cl, page):
    if page == cl.paginator.ELLIPSIS:
        extra_class = "disabled"
    elif page == cl.page_num:
        extra_class = "active"
    else:
        extra_class = ""

    url = cl.get_query_string({PAGE_VAR: page})

    return mark_safe(
        f"""<li class="paginate_button page-item {extra_class}"><a href="{url}"
            data-dt-idx="{page}" tabindex="{page}" class="page-link">{page}</a></li>"""
    )
