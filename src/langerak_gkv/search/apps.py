import os

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

DOCKER_BUILD = int(os.getenv("DOCKER_BUILD", "0"))


class Searchconfig(AppConfig):
    name = "langerak_gkv.search"

    def ready(self):
        from langerak_gkv.apphooks import ensure_apphook_installed
        from .cms_apps import SearchApp

        if DOCKER_BUILD:
            return

        ensure_apphook_installed(SearchApp, _("Search"))
