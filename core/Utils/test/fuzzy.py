import string
import secrets

from factory.fuzzy import BaseFuzzyAttribute, FuzzyText
from core.Utils.constants import PASSWORD_SPEC_SYMBOLS


class FuzzyPassword(BaseFuzzyAttribute):
    def __init__(self, length=12, **kwargs):
        self.length = length
        super().__init__(**kwargs)

    def fuzz(self):
        uppercase = secrets.choice(string.ascii_uppercase)
        lowercase = secrets.choice(string.ascii_lowercase)
        number = secrets.choice(string.digits)
        special = secrets.choice(PASSWORD_SPEC_SYMBOLS)

        password = ''.join([uppercase, lowercase, number, special])
        password += ''.join(
            secrets.choice(string.ascii_letters + string.digits) for _ in range(self.length - len(password)))
        chars = list(password)
        secrets.SystemRandom().shuffle(chars)
        return ''.join(chars)


class FuzzyColor(FuzzyText):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('prefix', '#')
        kwargs.setdefault('length', 6)
        kwargs.setdefault('chars', string.digits + 'ABCDEF')
        super().__init__(*args, **kwargs)
