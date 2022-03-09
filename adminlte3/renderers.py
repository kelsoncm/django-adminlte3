from django.template.backends.django import DjangoTemplates
from django.utils.functional import cached_property
from django.forms.renderers import BaseRenderer


class EngineMixin:
    def get_template(self, template_name):
        return self.engine.get_template(template_name)

    @cached_property
    def engine(self):
        return self.backend({
            'APP_DIRS': True,
            'DIRS': [],
            'NAME': 'djangoforms',
            'OPTIONS': {},
        })


class DjangoTemplatesRenderer(EngineMixin, BaseRenderer):
    """
    Load Django templates from the built-in widget templates in
    django/forms/templates and from apps' 'templates' directory.
    """
    backend = DjangoTemplates
