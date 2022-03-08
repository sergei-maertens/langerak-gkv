from datetime import datetime, time

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField


class ActivityManager(models.Manager):
    def _upcoming(self, **filters):
        date = timezone.now().date()
        return self.get_queryset().filter(
            Q(start_date__gte=date) | Q(end_date__gte=date, start_date__lt=date),
            **filters
        )

    def homepage(self):
        return self._upcoming(show_on_homepage=True)

    def upcoming(self, n=5, **filters):
        """
        Fetch the queryset for at most n upcoming activities
        """
        return (
            self._upcoming(**filters).order_by(
                "start_date",
                models.F("start_time").asc(nulls_first=True),
                "end_date",
                models.F("end_time").asc(nulls_last=True),
            )
        )[:n]


class Activity(models.Model):
    name = models.CharField(_("name"), max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, null=True)

    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"))
    start_time = models.TimeField(_("start time"), null=True, blank=True)
    end_time = models.TimeField(_("end time"), null=True, blank=True)

    intended_public = models.ForeignKey(
        "IntendedPublic", null=True, blank=True, on_delete=models.CASCADE
    )
    type = models.ForeignKey("ActivityType", on_delete=models.CASCADE)
    location = models.CharField(_("location"), max_length=255, blank=True)

    image = FilerImageField(blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(_("short description/intro"))
    content = PlaceholderField("content")
    show_on_homepage = models.BooleanField(
        default=False,
        help_text=_("If checked, this activity can appear on the homepage."),
    )

    url = models.URLField(_("external url"), blank=True)
    liturgy = models.ForeignKey(
        "liturgies.Liturgy", null=True, editable=False, on_delete=models.CASCADE
    )
    fb_event_id = models.CharField(_("facebook event id"), max_length=50, blank=True)

    objects = ActivityManager()

    class Meta:
        verbose_name = _("activity")
        verbose_name_plural = _("activities")
        ordering = ["start_date", "start_time", "end_date", "end_time"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.liturgy_id:
            return reverse(
                "liturgies:archive_date_detail",
                kwargs={
                    "year": self.start_date.year,
                    "month": self.start_date.month,
                    "day": self.start_date.day,
                    "pk": self.liturgy_id,
                },
            )
        return reverse("activities:detail", kwargs={"slug": self.slug})

    def clean(self):
        has_dates = self.start_date and self.end_date
        if has_dates and self.start_date > self.end_date:
            raise ValidationError(_("The start date cannot come before the end date."))

        has_times = self.start_time is not None and self.end_time is not None
        if (
            self.start_date == self.end_date
            and has_times
            and self.end_time < self.start_time
        ):
            raise ValidationError(_("The end time cannot come before the start time."))

        if self.show_on_homepage and not self.image:
            raise ValidationError(_("Homepage activities must have an image"))

    @property
    def start(self):
        start_time = self.start_time or time().replace(tzinfo=timezone.utc)
        return datetime.combine(self.start_date, start_time)

    @property
    def end(self):
        end_time = self.end_time or time().replace(tzinfo=timezone.utc)
        return datetime.combine(self.end_date, end_time)


class IntendedPublic(models.Model):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("intended public")
        verbose_name_plural = _("intended public")

    def __str__(self):
        return self.name


class ActivityType(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name
