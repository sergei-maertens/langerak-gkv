from django.utils.translation import gettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from langerak_gkv.utils.models import URLConfMenuEntry


class LiturgiesMenu(CMSAttachMenu):
    name = _("liturgies menu")

    def get_nodes(self, request):
        nodes = URLConfMenuEntry.objects.filter(app_name="liturgies").order_by("order")
        return [NavigationNode(node.display_name, node.resolve(), 1) for node in nodes]


menu_pool.register_menu(LiturgiesMenu)
