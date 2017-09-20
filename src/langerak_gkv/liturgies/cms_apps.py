from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import LiturgiesMenu


class LiturgiesApp(CMSApp):
    name = _('Liturgies')
    urls = ['langerak_gkv.liturgies.urls']
    menus = [LiturgiesMenu]


apphook_pool.register(LiturgiesApp)
