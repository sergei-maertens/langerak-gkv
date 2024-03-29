from django.utils.translation import gettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ActivitiesApp(CMSApp):
    name = _("Activities")
    app_name = "activities"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["langerak_gkv.activities.urls"]


apphook_pool.register(ActivitiesApp)
