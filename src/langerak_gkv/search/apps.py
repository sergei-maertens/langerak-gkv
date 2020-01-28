import os

from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

DOCKER_BUILD = int(os.getenv("DOCKER_BUILD", "0"))


class Searchconfig(AppConfig):
    name = "langerak_gkv.search"

    def ready(self):
        from cms.api import create_page
        from cms.models import Page
        from .cms_apps import SearchApp

        if DOCKER_BUILD:
            return

        search_pages = Page.objects.filter(
            application_urls="SearchApp", application_namespace=SearchApp.app_name
        )

        if not search_pages.exists():
            home = Page.objects.get_home()
            create_page(
                title=_("Search"),
                template=settings.CMS_TEMPLATES[0][0],
                language="nl",
                parent=home,
                apphook=SearchApp,
                apphook_namespace=SearchApp.app_name,
                published=True,
            )
