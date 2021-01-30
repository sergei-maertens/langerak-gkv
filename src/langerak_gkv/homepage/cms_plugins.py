from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CharFieldPlugin, HomepagePageLink


class HomepageLinkPlugin(CMSPluginBase):
    model = HomepagePageLink
    name = _("Homepage link block")
    raw_id_fields = ("page_link",)
    render_template = "homepage/cmsplugin/link.html"


plugin_pool.register_plugin(HomepageLinkPlugin)


class CharFieldPlugin(CMSPluginBase):
    model = CharFieldPlugin
    name = _("Simple text")
    render_template = "homepage/cmsplugin/charfield.html"


plugin_pool.register_plugin(CharFieldPlugin)
