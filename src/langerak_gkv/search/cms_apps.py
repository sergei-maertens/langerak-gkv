from django.utils.translation import gettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class SearchApp(CMSApp):
    name = _("Search")
    app_name = "search"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["langerak_gkv.search.urls"]


apphook_pool.register(SearchApp)
