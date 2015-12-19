from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = 'langerak_gkv.users'
    verbose_name = _('users')

    def ready(self):
        from . import signals  # noqa
