from django.utils.translation import gettext as _
from django.urls import path
from django.contrib.admin import ModelAdmin, register, site
# from django.contrib.admin import site
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin, sensitive_post_parameters_m, csrf_protect_m, transaction, router, settings, Http404, PermissionDenied, unquote, escape
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from .models import AllDataTypes


# site.unregister(User)


# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     search_fields = ('name',)
#     ordering = ('name',)
#     filter_horizontal = ('permissions',)

#     def formfield_for_manytomany(self, db_field, request=None, **kwargs):
#         if db_field.name == 'permissions':
#             qs = kwargs.get('queryset', db_field.remote_field.model.objects)
#             # Avoid a major performance hit resolving permission names which
#             # triggers a content_type load:
#             kwargs['queryset'] = qs.select_related('content_type')
#         return super().formfield_for_manytomany(db_field, request=request, **kwargs)


# @register(User)
# class UserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     # add_fieldsets = (
#     #     (None, {
#     #         'classes': ('wide',),
#     #         'fields': ('username', 'password1', 'password2'),
#     #     }),
#     # )
#     # add_form_template = 'admin/auth/user/add_form.html'
#     # change_user_password_template = None
#     # form = UserChangeForm
#     # add_form = UserCreationForm
#     # change_password_form = AdminPasswordChangeForm
#     # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
#     # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     # search_fields = ('username', 'first_name', 'last_name', 'email')
#     # ordering = ('username',)
#     # filter_horizontal = ('groups', 'user_permissions',)


@register(AllDataTypes)
class ModelAdmin(ModelAdmin):
    fieldsets = (
        (None, {"fields": ['char_field', 'text_field', 'slug_field']}),
        ('Number', {"fields": ['small_integer_field', 'integer_field', 'big_integer_field', 'positive_small_integer_field', 'positive_integer_field', 'positive_big_integer_field', 'decimal_field', 'float_field']}),
        ('Boolean', {"fields": ['desconhecido', 'sim', 'nao']}),
        ('Date & time', {"fields": ['date_field', 'time', 'date_time_field', 'duration_field']}),
        ('Net', {"fields": ['email_field', 'generic_ip_address_field', 'url_field']}),
        ('Extra', {"fields": ['json_field', 'uuid_field', 'file_path_field', 'file_field', 'image_field']}),
        ('Relational', {"fields": ['foreign_key_field', 'one_to_one_field', 'many_to_many_field']}),
    )
    
    autocomplete_fields = ['foreign_key_field', 'one_to_one_field']
