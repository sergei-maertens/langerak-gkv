from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class UsersApp(CMSApp):
    name = _('Users')
    urls = ['langerak_gkv.users.urls']


apphook_pool.register(UsersApp)
