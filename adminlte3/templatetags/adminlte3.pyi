from django.forms.fields import Field as Field
from django.utils.safestring import SafeString as SafeString

def quiet(field: Field): ...
def render_menu_list(menu_items: list, top_level: bool = ...) -> SafeString: ...
def page_item(cl, page): ...
