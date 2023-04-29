# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import PAGE_VAR
from django.template.defaultfilters import register
from django.forms.fields import Field


@register.filter(is_safe=False)
# @stringfilter
def quiet(field: Field):
    return ""


def __concatenate(to: str, check: bool, value: str, otherwise: str = ""):
    to += value if check else otherwise


@register.simple_tag
def render_menu_list(menu_items: list, top_level=True) -> str:
    result = ""
    __concatenate(result, not top_level, '<ul class="nav nav-treeview" style="display: none;">')
    for menu_item in menu_items:
        subitens = menu_item.get("subitens", None)
        badge = menu_item.get("badge", None)
        is_active = ""
        color = ""
        if menu_item.get("icon", None):
            icon = menu_item["icon"]
        elif menu_item.get("url", None):
            icon = "nav-icon far fa-circle"

        __concatenate(is_active, menu_item.get("active", False), "active")
        __concatenate(color, menu_item.get("color", None) is not None, menu_item["color"])

        __concatenate(result, menu_item.get("url", None), '<li class="nav-item">', '<li class="nav-header">')
        __concatenate(result, menu_item.get("url", None), f'<a href="{menu_item["url"]}" class="nav-link{is_active}">')
        __concatenate(result, True, f'<i class="nav-icon {icon} {color}"></i>')
        __concatenate(result, True, "<p>")
        __concatenate(result, True, menu_item.get("label", "-"))
        __concatenate(
            result,
            badge is not None,
            f'<span class="badge {badge.get("color", "")} right">{badge.get("label", "")}</span>',
        )
        __concatenate(result, subitens, '<i class="right fas fa-angle-left"></i>')
        __concatenate(result, True, "</p>")
        __concatenate(result, menu_item.get("url", None), "</a>")
        __concatenate(result, subitens, render_menu_list(subitens, False))
        __concatenate(result, True, "</li>")
    __concatenate(result, not top_level, "</ul>")
    return mark_safe(result)


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
