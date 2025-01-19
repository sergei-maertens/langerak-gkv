import os

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from djangocms_text_ckeditor.fields import HTMLField


class Church(models.Model):
    name = models.CharField(_("name"), max_length=100)
    auto_selected = models.BooleanField(
        _("automatically selected"),
        default=False,
        help_text=_("If checked, liturgies will by default be related to this church."),
    )

    class Meta:
        verbose_name = _("church")
        verbose_name_plural = _("churches")

    def __str__(self):
        return self.name


def get_default_churches():
    return Church.objects.filter(auto_selected=True)


class Liturgy(models.Model):
    date = models.DateField(_("date"))
    service = models.ForeignKey(
        "Service", verbose_name=_("service"), on_delete=models.CASCADE
    )
    preacher = models.CharField(_("preacher"), max_length=100, blank=True)
    bible_readings = models.TextField(_("Bible readings"), blank=True)
    service_theme = models.CharField(_("service theme"), max_length=255, blank=True)
    liturgy = HTMLField(pgettext_lazy("admin field", "liturgy"), blank=True)
    download = models.URLField(
        _("download"),
        blank=True,
        help_text=_("Download link"),
    )
    audiofile = models.FileField(
        _("audiofile"),
        upload_to="liturgies/audio",
        max_length=100,
        blank=True,
        editable=False,
        help_text=_(
            "Audio downloads are no longer available as of Jan. 31st - this field has "
            "been disabled."
        ),
    )
    collection_goal1 = models.CharField(
        _("collection goal 1"), max_length=50, blank=True
    )
    collection_goal2 = models.CharField(
        _("collection goal 2"), max_length=50, blank=True
    )
    collection_goal3 = models.CharField(
        _("collection goal 3"), max_length=50, blank=True
    )
    extra_information = models.TextField(_("extra information"), blank=True)

    other_churches = models.ManyToManyField(
        "Church",
        verbose_name=_("other churches"),
        blank=True,
        default=get_default_churches,
    )

    class Meta:
        verbose_name = _("liturgy")
        verbose_name_plural = _("liturgies")
        ordering = ["-date"]

    def __str__(self):
        return "{service} {date}".format(
            service=self.service.name, date=self.date.strftime("%d-%m-%Y")
        )

    def get_absolute_url(self):
        return reverse(
            "liturgies:archive_date_detail",
            kwargs={
                "year": self.date.year,
                "month": self.date.month,
                "day": self.date.day,
                "pk": self.pk,
            },
        )

    def get_collections(self):
        collections = []
        if self.collection_goal1:
            collections.append(self.collection_goal1)
        if self.collection_goal2:
            collections.append(self.collection_goal2)
        if self.collection_goal3:
            collections.append(self.collection_goal3)
        return collections

    @property
    def part_of_day(self):
        """
        Returns the string representation of the part of the day when the liturgy happens.

        E.g. 'morning', 'afternoon', 'evening'
        """
        service_time = self.service.time
        if service_time.hour < 12:
            return _("morning")
        elif service_time.hour < 17:
            return _("afternoon")
        return _("evening")

    @property
    def download_file_name(self) -> str:
        if not self.download:
            return ""
        return os.path.basename(self.download.name)


class Service(models.Model):
    name = models.CharField(_("service name"), max_length=50)
    time = models.TimeField(_("service time"))

    def __str__(self):
        return self.name
