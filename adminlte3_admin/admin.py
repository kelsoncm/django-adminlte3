
from django.contrib.admin import ModelAdmin
from django.db import models
from django import forms
from adminlte3_admin.widgets import (
    AdminLTEDateWidget, AdminLTETimeWidget, AdminLTESplitDateTime,
    AdminLTERadioSelect, AdminLTEFileWidget, AdminLTEForeignKeyRawIdWidget,
    AdminLTEManyToManyRawIdWidget, AdminLTERelatedFieldWidgetWrapper, 
    AdminLTETextareaWidget, AdminLTETextInputWidget, AdminLTEEmailInputWidget,
    AdminLTEURLFieldWidget, AdminLTEIntegerFieldWidget, 
    AdminLTEBigIntegerFieldWidget, AdminLTEAutocompleteMixin, 
    AdminLTEAutocompleteSelect, AdminLTEAutocompleteSelectMultiple, 
    AdminLTEUUIDInputWidget
)

ModelAdmin.formfield_overrides = {
    models.DateTimeField: {'form_class': forms.SplitDateTimeField, 'widget': AdminLTESplitDateTime},
    models.DateField: {'widget': AdminLTEDateWidget},
    models.TimeField: {'widget': AdminLTETimeWidget},
    models.TextField: {'widget': AdminLTETextareaWidget},
    models.URLField: {'widget': AdminLTEURLFieldWidget},
    models.IntegerField: {'widget': AdminLTEIntegerFieldWidget},
    models.BigIntegerField: {'widget': AdminLTEBigIntegerFieldWidget},
    models.CharField: {'widget': AdminLTETextInputWidget},
    models.ImageField: {'widget': AdminLTEFileWidget},
    models.FileField: {'widget': AdminLTEFileWidget},
    models.EmailField: {'widget': AdminLTEEmailInputWidget},
    # models.UUIDField: {'widget': AdminLTEUUIDInputWidget},
}