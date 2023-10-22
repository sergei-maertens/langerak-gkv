from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LiturgiesConfig(AppConfig):
    name = "langerak_gkv.liturgies"
    verbose_name = _("liturgies")

    def ready(self):
        from . import signals  # noqa
