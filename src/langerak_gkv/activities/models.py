from datetime import datetime, time

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from cms.models.fields import PlaceholderField


class ActivityManager(models.Manager):

    def upcoming(self, n=5):
        """
        Fetch the queryset for at most n upcoming activities
        """
        date = timezone.now().date()
        return self.filter(
            Q(start_date__gte=date) | Q(end_date__gte=date, start_date__lt=date)
        ).order_by('start_date', 'end_date')[:n]


class Activity(models.Model):
    name = models.CharField(_('name'), max_length=100)

    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    start_time = models.TimeField(_('start time'), null=True, blank=True)
    end_time = models.TimeField(_('end time'), null=True, blank=True)

    intended_public = models.ForeignKey('IntendedPublic', null=True, blank=True)
    type = models.ForeignKey('ActivityType')
    location = models.CharField(_('location'), max_length=255, blank=True)

    description = models.TextField(_('short description/intro'))
    content = PlaceholderField('content')

    url = models.URLField(_('external url'), blank=True)
    liturgy = models.ForeignKey('liturgies.Liturgy', null=True, editable=False)
    fb_event_id = models.CharField(_('facebook event id'), max_length=50, blank=True)

    objects = ActivityManager()

    class Meta:
        verbose_name = _(u'activity')
        verbose_name_plural = _(u'activities')
        ordering = ['start_date', 'start_time', 'end_date', 'end_time']

    def __unicode__(self):
        return self.name

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError(_('The start date cannot come before the end date.'))

        if self.start_date == self.end_date and self.end_time < self.start_time:
            raise ValidationError(_('The end time cannot come before the start time.'))

    @property
    def start(self):
        start_time = self.start_time or time().replace(tzinfo=timezone.utc)
        return datetime.combine(self.start_date, start_time)

    @property
    def end(self):
        end_time = self.end_time or time().replace(tzinfo=timezone.utc)
        return datetime.combine(self.end_date, end_time)


class IntendedPublic(models.Model):
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _(u'intended public')
        verbose_name_plural = _(u'intended public')

    def __unicode__(self):
        return self.name


class ActivityType(models.Model):
    name = models.CharField(_('name'), max_length=100)

    def __unicode__(self):
        return self.name
