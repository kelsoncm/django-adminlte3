from django.utils.safestring import mark_safe
from django import template


register = template.Library()


@register.simple_tag
def render_menu_list(menu_items: list, top_level=True) -> str:
    result = ""
    result += f'<ul class="nav nav-treeview" style="display: none;">' if not top_level else ''
    for menu_item in menu_items:
        subitens = menu_item.get('subitens', None)
        badge = menu_item.get('badge', None)
        is_active = 'active' if menu_item.get('active', False) else ''
        color = menu_item["color"] if menu_item.get("color", None) is not None else f''
        if menu_item.get("icon", None):
            icon = menu_item["icon"]
        else:
            icon = 'nav-icon far fa-circle' if menu_item.get('url', None) else ''

        result += '<li class="nav-item">' if menu_item.get('url', None) else '<li class="nav-header">'
        result += f'<a href="{menu_item["url"]}" class="nav-link{is_active}">' if menu_item.get('url', None) else ''
        result += f'<i class="nav-icon {icon} {color}"></i>' 
        result += f'<p>'
        result += menu_item.get("label", '-')
        result += f'<span class="badge {badge.get("color", "")} right">{badge.get("label", "")}</span>' if badge is not None else ''
        result += f'<i class="right fas fa-angle-left"></i>' if subitens else ''
        result += f'</p>'
        result += f'</a>' if menu_item.get('url', None) else ''
        result += render_menu_list(subitens, False) if subitens else ''
        result += f'</li>'
    result += f'</ul>' if not top_level else ''
    return mark_safe(result)
