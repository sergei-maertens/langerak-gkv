from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LogEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='worklogentry_set')
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'))
    log_message = models.CharField(_('log_message'), max_length=512)

    paid = models.BooleanField(_('paid?'), default=False)

    class Meta:
        verbose_name = _(u'log entry')
        verbose_name_plural = _(u'log entries')
        ordering = ('-end', '-start')

    def time_spent(self):
        seconds = (self.end - self.start).seconds
        hours = seconds / 3600
        seconds = seconds - (hours * 3600)
        minutes = seconds / 60
        return "{hours}:{minutes}".format(hours=hours, minutes=minutes)
