from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SocietyPlugin


class SocietyPlugin(CMSPluginBase):
    model = SocietyPlugin
    name = _("Society")
    module = _("Societies")
    raw_id_fields = ("society",)
    render_template = "societies/cmsplugin/society.html"


plugin_pool.register_plugin(SocietyPlugin)
