from typing import Union, Any
from django.forms.widgets import Widget
from django.contrib.admin.sites import AdminSite
from django.core.validators import BaseValidator, URLValidator
from django.db.models.fields import Field
from django.contrib.admin.widgets import (
    AdminDateWidget,
    AdminTimeWidget,
    AdminSplitDateTime,
    AdminRadioSelect,
    AdminFileWidget,
    ForeignKeyRawIdWidget,
    ManyToManyRawIdWidget,
    RelatedFieldWidgetWrapper,
    AdminTextareaWidget,
    AdminTextInputWidget,
    AdminEmailInputWidget,
    AdminURLFieldWidget,
    AdminIntegerFieldWidget,
    AdminBigIntegerFieldWidget,
    AutocompleteMixin,
    AutocompleteSelect,
    AutocompleteSelectMultiple,
)

class AdminLTEDateWidget(AdminDateWidget):
    def __init__(self, attrs: Union[dict, None] = None, format: Union[str, None] = None): ...

class AdminLTESplitDateTime(AdminSplitDateTime):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTERadioSelect(AdminRadioSelect):
    def __init__(self, attrs: Union[dict, None] = None, choices: tuple = ()): ...

class AdminLTEFileWidget(AdminFileWidget):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTEForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    def __init__(
        self, rel: Any, admin_site: AdminSite, attrs: Union[dict, None] = None, using: Union[Any, None] = None
    ): ...

class AdminLTEManyToManyRawIdWidget(ManyToManyRawIdWidget):
    def __init__(self, name: str, value: Any, attrs: Union[dict, None] = None): ...

class AdminLTERelatedFieldWidgetWrapper(RelatedFieldWidgetWrapper):
    def __init__(
        self,
        widget: Widget,
        rel: Any,
        admin_site: AdminSite,
        can_add_related: Union[Any, None] = None,
        can_change_related: bool = False,
        can_delete_related: bool = False,
        can_view_related: bool = False,
    ): ...

class AdminLTETimeWidget(AdminTimeWidget):
    def __init__(self, attrs: Union[dict, None] = None, format: Union[str, None] = None): ...

class AdminLTETextareaWidget(AdminTextareaWidget):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTETextInputWidget(AdminTextInputWidget):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTEEmailInputWidget(AdminEmailInputWidget):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTEURLFieldWidget(AdminURLFieldWidget):
    def __init__(self, attrs: Union[dict, None] = None, validator_class: BaseValidator = URLValidator): ...

class AdminLTEIntegerFieldWidget(AdminIntegerFieldWidget):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTEBigIntegerFieldWidget(AdminBigIntegerFieldWidget):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTEUUIDInputWidget(AutocompleteMixin):
    def __init__(self, attrs: Union[dict, None] = None): ...

class AdminLTEAutocompleteSelect(AutocompleteSelect):
    def __init__(
        self,
        field: Field,
        admin_site: AdminSite,
        attrs: Union[dict, None] = None,
        choices: tuple = (),
        using: Union[Any, None] = None,
    ): ...

class AdminLTEAutocompleteSelectMultiple(AutocompleteSelectMultiple):
    def __init__(
        self,
        field: Field,
        admin_site: AdminSite,
        attrs: Union[dict, None] = None,
        choices: tuple = (),
        using: Union[Any, None] = None,
    ): ...
