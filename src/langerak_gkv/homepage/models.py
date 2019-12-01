from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

_IMG_SIZE = settings.THUMBNAIL_ALIASES[""]["homepage"]["size"]


class PrayerOnDemand(models.Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"))
    body = models.TextField(_("What should we pray for?"))
    replied = models.BooleanField(_("replied"), default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("prayer on demand")
        verbose_name_plural = _("prayer on demands")

    def __str__(self):
        return self.name


class HomepagePageLink(CMSPlugin):
    title = models.CharField(_("title"), max_length=50)
    image = FilerImageField(
        verbose_name=_("image"),
        on_delete=models.CASCADE,
        help_text=_(
            "Block image - note that only rows 1 and 3 display images. "
            f"Images will be cropped to {_IMG_SIZE[0]}x{_IMG_SIZE[1]}"
        ),
        blank=True,
        null=True,
    )
    description = HTMLField(_("description"), help_text=_("Displayed below the title"))
    page_link = PageField(
        verbose_name=_("page"), blank=True, null=True, help_text=_("Page to link to")
    )

    def __str__(self):
        return f"{self.title} - {self.page_link }"


class CharFieldPlugin(CMSPlugin):
    content = models.CharField(_("text"), max_length=255)

    def __str__(self):
        return self.content
