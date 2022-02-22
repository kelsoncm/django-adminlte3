
from django.contrib.admin import widgets, ModelAdmin
from django.db import models
from django import forms

class MyAdminTextInputWidget(widgets.AdminTextInputWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'form-control', **(attrs or {})})


ModelAdmin.formfield_overrides = {
        models.DateTimeField: {'form_class': forms.SplitDateTimeField, 'widget': MyAdminTextInputWidget    },
        models.DateField: {'widget': MyAdminTextInputWidget},
        models.TimeField: {'widget': MyAdminTextInputWidget},
        models.TextField: {'widget': MyAdminTextInputWidget},
        models.URLField: {'widget': MyAdminTextInputWidget},
        models.IntegerField: {'widget': MyAdminTextInputWidget},
        models.BigIntegerField: {'widget': MyAdminTextInputWidget},
        models.CharField: {'widget': MyAdminTextInputWidget},
        models.ImageField: {'widget': MyAdminTextInputWidget},
        models.FileField: {'widget': MyAdminTextInputWidget},
        models.EmailField: {'widget': MyAdminTextInputWidget},
        models.UUIDField: {'widget': MyAdminTextInputWidget},
    }    
