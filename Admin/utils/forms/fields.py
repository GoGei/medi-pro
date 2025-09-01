from django import forms
from django.core.validators import RegexValidator


class ColorField(forms.CharField):
    widget = forms.ColorInput
    default_validators = [
        RegexValidator(regex=r'#[0-9a-fA-F]{6}')
    ]

    def to_python(self, value):
        return value.upper()
