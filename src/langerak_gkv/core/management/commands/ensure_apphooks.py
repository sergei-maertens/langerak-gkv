from django.core.management import BaseCommand

from langerak_gkv.activities.cms_apps import ActivitiesApp
from langerak_gkv.apphooks import ensure_apphook_installed
from langerak_gkv.liturgies.cms_apps import LiturgiesApp
from langerak_gkv.search.cms_apps import SearchApp


class Command(BaseCommand):
    help = "Ensure all the expected apphooks are installed"

    def handle(self, **options):
        for app in [ActivitiesApp, LiturgiesApp, SearchApp]:
            ensure_apphook_installed(app)
