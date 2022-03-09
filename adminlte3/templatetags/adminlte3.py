from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import PAGE_VAR
from django.template.defaultfilters import stringfilter, register
from django.forms.fields import Field


@register.filter(is_safe=False)
# @stringfilter
def quiet(field: Field):
    return ''

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
    
@register.simple_tag
def page_item(cl, page):
    
    if page == cl.paginator.ELLIPSIS:
        extra_class = 'disabled'
    elif page == cl.page_num:
        extra_class = 'active'
    else:
        extra_class = ''

    url = cl.get_query_string({PAGE_VAR: page})
        
    return mark_safe(f'''<li class="paginate_button page-item {extra_class}"><a href="{url}" data-dt-idx="{page}" tabindex="{page}" class="page-link">{page}</a></li>''')
    
