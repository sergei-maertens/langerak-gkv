from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PlaceholderField


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

    class Meta:
        verbose_name = _(u'activity')
        verbose_name_plural = _(u'activities')
        ordering = ['start_date', 'start_time', 'end_date', 'end_time']

    def __unicode__(self):
        return self.name


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
