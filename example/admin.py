from django.contrib.admin import register, ModelAdmin
from .models import AllDataTypes


@register(AllDataTypes)
class ModelAdmin(ModelAdmin):
    pass
