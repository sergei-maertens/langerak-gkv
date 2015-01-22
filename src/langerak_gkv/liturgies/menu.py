from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool


class LiturgiesMenu(CMSAttachMenu):

    name = _('liturgies menu')

    def get_nodes(self, request):
        return [
            NavigationNode(_('Liturgy history'), reverse('liturgies:history'), 1)
        ]


menu_pool.register_menu(LiturgiesMenu)
