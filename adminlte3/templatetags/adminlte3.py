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


def __concatenate(check: bool, value: str, otherwise: str = ""):
    return value if check else otherwise


@register.simple_tag
def render_menu_list(menu_items: list, top_level=True) -> SafeString:
    if len(menu_items) == 0:
        return mark_safe("")
    result = __concatenate(not top_level, '<ul class="nav nav-treeview">')
    for menu_item in menu_items:
        url = menu_item.get("url", None)
        is_active = menu_item.get("active", "")
        color = menu_item.get("color", "")
        icon = menu_item.get("icon", "1")
        badge = menu_item.get("badge", {})
        subitens = menu_item.get("subitens", [])

        result += __concatenate(url is not None, '<li class="nav-item">', '<li class="nav-header">')
        result += __concatenate(url is not None, f'<a href="{url}" class="nav-link {is_active}">')
        result += __concatenate(True, f'<i class="nav-icon {icon} {color}"></i>')
        result += __concatenate(True, "<p>")
        result += __concatenate(True, menu_item.get("label", "-"))
        result += __concatenate(
            len(badge.keys()) > 0,
            f'<span class="badge {badge.get("color", "")} right">{badge.get("label", "")}</span>',
        )
        result += __concatenate(len(subitens) > 0, '<i class="right fas fa-angle-left"></i>')
        result += __concatenate(True, "</p>")
        result += __concatenate(url is not None, "</a>")
        result += __concatenate(len(subitens) > 0, render_menu_list(subitens, False))
        result += __concatenate(True, "</li>")
    result += __concatenate(not top_level, "</ul>")
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
