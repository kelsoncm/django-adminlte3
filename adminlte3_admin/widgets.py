from django.contrib.admin.widgets import (
    AdminDateWidget, AdminTimeWidget, AdminSplitDateTime, AdminRadioSelect, 
    AdminFileWidget, ForeignKeyRawIdWidget, ManyToManyRawIdWidget, 
    RelatedFieldWidgetWrapper, AdminTextareaWidget, AdminTextInputWidget, 
    AdminEmailInputWidget, AdminURLFieldWidget, AdminIntegerFieldWidget, 
    AdminBigIntegerFieldWidget, AutocompleteMixin, AutocompleteMixin, 
    AutocompleteSelect, AutocompleteSelectMultiple 
)

class AdminLTEDateWidget(AdminDateWidget):
    pass
    # def __init__(self, attrs=None, format=None):
    #     attrs = {'class': 'form-control', 'size': '10', **(attrs or {})}
    #     super().__init__(attrs=attrs, format=format)


class AdminLTETimeWidget(AdminTimeWidget):
    def __init__(self, attrs=None, format=None):
        attrs = {'class': 'form-control', 'size': '8', **(attrs or {})}
        super().__init__(attrs=attrs, format=format)


class AdminLTESplitDateTime(AdminSplitDateTime):
    pass


class AdminLTERadioSelect(AdminRadioSelect):
    pass


class AdminLTEFileWidget(AdminFileWidget):
    pass


class AdminLTEForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    pass


class AdminLTEManyToManyRawIdWidget(ManyToManyRawIdWidget):
    pass


class AdminLTERelatedFieldWidgetWrapper(RelatedFieldWidgetWrapper):
    pass


class AdminLTETextareaWidget(AdminTextareaWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


class AdminLTETextInputWidget(AdminTextInputWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


class AdminLTEEmailInputWidget(AdminEmailInputWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


class AdminLTEURLFieldWidget(AdminURLFieldWidget):
    pass


class AdminLTEIntegerFieldWidget(AdminIntegerFieldWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


class AdminLTEBigIntegerFieldWidget(AdminBigIntegerFieldWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


class AdminLTEUUIDInputWidget(AutocompleteMixin):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


class AdminLTEAutocompleteMixin(AutocompleteMixin):
    pass


class AdminLTEAutocompleteSelect(AutocompleteSelect):
    pass


class AdminLTEAutocompleteSelectMultiple(AutocompleteSelectMultiple):
    pass

