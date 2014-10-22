from django.db import models
from django.utils.translation import ugettext_lazy as _


class PrayerOnDemand(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'))
    body = models.TextField(_('What should we pray for?'))
    replied = models.BooleanField(_('replied'), default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'prayer on demand')
        verbose_name_plural = _(u'prayer on demands')

    def __unicode__(self):
        return self.name
