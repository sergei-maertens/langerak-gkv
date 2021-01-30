from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField, PlaceholderField


@python_2_unicode_compatible
class Society(models.Model):
    name = models.CharField(_("name"), max_length=255)
    content = PlaceholderField("content")

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    class Meta:
        verbose_name = _("society")
        verbose_name_plural = _("societies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("societies:detail", kwargs={"pk": self.pk})


@python_2_unicode_compatible
class SocietyPlugin(CMSPlugin):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    page_link = PageField(
        verbose_name=_("page"), blank=True, null=True, help_text=_("Page to link to")
    )

    def __str__(self):
        return self.society.name
