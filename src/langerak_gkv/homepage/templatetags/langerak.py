import logging

from django import template
from django.template.defaultfilters import stringfilter
from django.urls import NoReverseMatch, reverse
from django.utils.module_loading import import_string

from langerak_gkv.activities.models import Activity

from ..forms import PrayerOnDemandForm

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
@stringfilter
def active(path, reverse_name, exact=False):
    try:
        url = reverse(reverse_name)
    except NoReverseMatch as e:
        if reverse_name == "home":
            url = "/"
        else:
            logger.debug(e)
            return False

    if path == url and exact:
        return True
    elif path.startswith(url) and not exact and path != "/":
        return True
    return False


@register.filter
@stringfilter
def active_exact(path, reverse_name):
    return active(path, reverse_name, exact=True)


@register.simple_tag
def get_activities():
    qs = Activity.objects.homepage().order_by("?")[:4]
    return list(qs)


@register.simple_tag
def get_pod_form(request):
    return PrayerOnDemandForm(request=request)


@register.simple_tag
def ensure_apphook(cms_app: str) -> str:
    """
    Ensure an apphook is installed.
    """
    from langerak_gkv.apphooks import ensure_apphook_installed

    apphook_cls = import_string(cms_app)
    ensure_apphook_installed(apphook_cls)
    return ""
