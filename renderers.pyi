from django.forms.renderers import BaseRenderer
from django.template.backends.django import DjangoTemplates

class EngineMixin:
    def get_template(self, template_name): ...
    def engine(self): ...

class DjangoTemplatesRenderer(EngineMixin, BaseRenderer):
    backend = DjangoTemplates
