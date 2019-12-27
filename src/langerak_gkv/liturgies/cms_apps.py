from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import LiturgiesMenu


class LiturgiesApp(CMSApp):
    name = _("Liturgies")
    app_name = "liturgies"

    def get_menus(self, page=None, language=None, **kwargs):
        return [LiturgiesMenu]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["langerak_gkv.liturgies.urls"]


apphook_pool.register(LiturgiesApp)
