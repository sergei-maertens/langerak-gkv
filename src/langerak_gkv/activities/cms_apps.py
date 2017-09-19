from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ActivitiesApp(CMSApp):
    name = _('Activities')
    urls = ['langerak_gkv.activities.urls']


apphook_pool.register(ActivitiesApp)
