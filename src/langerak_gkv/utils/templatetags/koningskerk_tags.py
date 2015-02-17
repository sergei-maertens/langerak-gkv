from django import template

register = template.Library()


@register.filter
def pop(value, index=0):
    if isinstance(value, list) and len(value) > 0:
        return value.pop(index)
    return None
