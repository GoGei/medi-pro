import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _


class IsActiveField(django_filters.ChoiceFilter):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('choices', (
            ('', '---------'),
            ('true', _('Active')),
            ('false', _('Not active')),
        ))
        kwargs.setdefault('empty_label', None)
        kwargs.setdefault('widget', forms.Select)
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        if value == 'true':
            return qs.filter(**{self.field_name: True})
        elif value == 'false':
            return qs.filter(**{self.field_name: False})
        return qs


class IsActiveMixinField(IsActiveField):
    def filter(self, qs, value):
        if value == 'true':
            return qs.active()
        elif value == 'false':
            return qs.not_active()
        return qs
