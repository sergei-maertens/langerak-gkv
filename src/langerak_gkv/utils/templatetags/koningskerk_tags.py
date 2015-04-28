from django import template

register = template.Library()


@register.filter
def pop(value, index=0):
    if isinstance(value, list) and len(value) > 0:
        return value.pop(index)
    return None


@register.simple_tag(takes_context=True)
def absolute_url(context, location=None):
    return context['request'].build_absolute_uri(location)
