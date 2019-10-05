from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class PrayerOnDemand(models.Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"))
    body = models.TextField(_("What should we pray for?"))
    replied = models.BooleanField(_("replied"), default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u"prayer on demand")
        verbose_name_plural = _(u"prayer on demands")

    def __unicode__(self):
        return self.name


class HomepagePageLink(CMSPlugin):
    title = models.CharField(_("title"), max_length=50)
    image = FilerImageField(verbose_name=_("image"), on_delete=models.CASCADE)
    description = HTMLField(_("description"), help_text=_("Displayed below the title"))
    page_link = PageField(
        verbose_name=_("page"), blank=True, null=True, help_text=_("Page to link to")
    )
    enable_sharing = models.BooleanField(_("enable social sharing"), default=True)

    def __unicode__(self):
        return u"{0} - {1}".format(self.title, self.page_link)


class CharFieldPlugin(CMSPlugin):
    content = models.CharField(_("text"), max_length=255)

    def __unicode__(self):
        return self.content
