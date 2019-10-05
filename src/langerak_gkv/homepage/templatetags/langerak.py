import logging

from django import template
from django.urls import NoReverseMatch, reverse
from django.template.defaultfilters import stringfilter

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
@stringfilter
def active(path, reverse_name, exact=False):
    try:
        url = reverse(reverse_name)
    except NoReverseMatch as e:
        logger.debug(e)
        return False

    if path == url and exact:
        return True
    elif path.startswith(url) and not exact and path != reverse('home'):
        return True
    return False


@register.filter
@stringfilter
def active_exact(path, reverse_name):
    return active(path, reverse_name, exact=True)
