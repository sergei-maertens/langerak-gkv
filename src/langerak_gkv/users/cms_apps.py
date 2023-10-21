from django.utils.translation import gettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class UsersApp(CMSApp):
    name = _("Users")
    app_name = "users"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["langerak_gkv.users.urls"]


apphook_pool.register(UsersApp)
