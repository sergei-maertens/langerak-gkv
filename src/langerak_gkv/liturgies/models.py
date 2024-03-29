import os

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from djangocms_text_ckeditor.fields import HTMLField


class Church(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name


class Liturgy(models.Model):
    date = models.DateField(_("date"))
    service = models.ForeignKey(
        "Service", verbose_name=_("service"), on_delete=models.CASCADE
    )
    preacher = models.CharField(_("preacher"), max_length=100, blank=True)
    preach_author = models.CharField(_("preach author"), max_length=100, blank=True)
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
    beamist = models.CharField(
        _("beamist"), max_length=50, blank=True
    )  # search on function: beamists
    organist = models.CharField(
        _("organist"), max_length=50, blank=True
    )  # searches on function: organists
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
        "Church", verbose_name=_("other churches"), blank=True
    )

    internal_remarks = models.TextField(_("remarks (internal)"), blank=True)

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


class MailRecipient(models.Model):
    class Functions(models.TextChoices):
        preacher = "0preacher", _("preacher (%s)") % settings.EMAIL_PREACHER
        koster = "koster", _("koster (%s)") % settings.EMAIL_KOSTER
        beamist = "2beamist", _("beamist (%s)") % settings.EMAIL_BEAMIST
        organist = "1organist", _("organist (%s)") % settings.EMAIL_ORGANIST
        bible_goup = "biblegroup", _("bible group (%s)" % settings.EMAIL_BIBLE_GROUP)
        preach_creation = (
            "preach_creation",
            _("preach creation (%s)" % settings.EMAIL_PREACH_CREATION),
        )

    liturgy = models.ForeignKey(
        "Liturgy", verbose_name=_("liturgy"), on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        max_length=100,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(max_length=254, blank=True)
    function = models.CharField(choices=Functions.choices, max_length=50, blank=True)
    is_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ["function"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk and not self.email:
            self.email = self.get_email()
        super(MailRecipient, self).save(*args, **kwargs)

    def get_email(self):
        if self.email:
            return self.email
        if self.user and self.user.email:
            return self.user.email

        value_to_attr = dict(zip(self.Functions.values, self.Functions.names))
        attr = value_to_attr.get(self.function)
        if attr is not None:
            email = getattr(settings, "EMAIL_%s" % attr.upper(), None)
            if email is not None:
                return email
        raise ValueError("Could not determine e-mail address")
