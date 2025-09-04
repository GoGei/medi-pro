from django import template

register = template.Library()


@register.filter(name='get_class')
def get_class(value):
    return value.__class__.__name__


@register.filter(name='is_in')
def inlist(value, args):
    if args is None:
        return False
    _list = [arg.strip() for arg in args.split(',')]
    return value in _list


@register.filter(name="get_attr")
def get_attr(obj, attr):
    return getattr(obj, attr, None)
