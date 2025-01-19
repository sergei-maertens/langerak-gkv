from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def absolute_url(context, location=None):
    return context["request"].build_absolute_uri(location)
