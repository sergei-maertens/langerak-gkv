from django.contrib.auth import get_user_model
from django.utils.dates import MONTHS
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


@plugin_pool.register_plugin
class BirthdayCalendarPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _('Birthday calendar')
    render_template = 'users/cmsplugin/birthdays.html'

    def render(self, context, instance, placeholder):
        context = super(BirthdayCalendarPlugin, self).render(context, instance, placeholder)

        User = get_user_model()
        # Extracts/Truncates are only avaible in Django 1.10+
        users = list(User.objects.filter(birthdate__isnull=False))
        users.sort(key=lambda u: (u.birthdate.month, u.birthdate.day))
        context['profiles'] = users
        context['months'] = [m[1] for m in sorted(MONTHS.items())]
        return context
