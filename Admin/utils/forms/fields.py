from django import forms
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import (
    BaseValidator, MinLengthValidator, MaxLengthValidator, ProhibitNullCharactersValidator, RegexValidator
)
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


class ColorField(forms.CharField):
    widget = forms.ColorInput
    default_validators = [
        RegexValidator(regex=r'#[0-9a-fA-F]{6}')
    ]

    def to_python(self, value):
        return value.upper()


@deconstructible
class ContainsLowerCaseValidator:
    message = _('Value must contains lowercase characters.')
    code = 'not_contains_lowercase'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not any(c.islower() for c in str(value)):
            raise ValidationError(self.message, code=self.code, params={'value': value})

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.message == other.message and self.code == other.code


@deconstructible
class ContainsUpperCaseValidator:
    message = _('Value must contains uppercase characters.')
    code = 'not_contains_uppercase'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not any(c.isupper() for c in str(value)):
            raise ValidationError(self.message, code=self.code, params={'value': value})

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.message == other.message and self.code == other.code


@deconstructible
class ContainsSpecialCharactersCaseValidator:
    message = _('Value must contains special characters: %(chars)s.')
    code = 'not_contains_special_chars'
    chars = '!@#$%^&*'

    def __init__(self, message=None, code=None, chars: str = None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if chars is not None:
            self.chars = chars

    def __call__(self, value):
        if not any(c in self.chars for c in str(value)):
            raise ValidationError(self.message, code=self.code, params={'value': value, 'chars': self.chars})

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.message == other.message and self.code == other.code


@deconstructible
class ASCIIOnlyValidator:
    message = _('Value must contain only ASCII characters.')
    code = 'not_ascii_only'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        try:
            str(value).encode('ascii')
        except UnicodeEncodeError:
            raise ValidationError(self.message, code=self.code, params={'value': value})

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.message == other.message and self.code == other.code


class PasswordField(forms.CharField):
    widget = forms.PasswordInput
    default_validators = [
        MinLengthValidator(limit_value=8, message=_('Password must contains at least 8 characters')),
        MaxLengthValidator(limit_value=32, message=_('Password must contains at most 32 characters')),
        ProhibitNullCharactersValidator(message=_('It is not allowed to have spaces')),
        ContainsLowerCaseValidator(message=_('Password must contains lowercase characters')),
        ContainsUpperCaseValidator(message=_('Password must contains uppercase characters')),
        ContainsSpecialCharactersCaseValidator(message=_('Password must contains special characters: %(chars)s.')),
        ASCIIOnlyValidator(message=_('Password must contains only ASCII characters')),
    ]

    def run_validators(self, value):
        errors = []
        for v in self.default_validators:
            try:
                v(value)
            except ValidationError as e:
                errors.extend(e.error_list)
        if errors:
            raise ValidationError(errors)
