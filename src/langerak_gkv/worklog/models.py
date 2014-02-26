from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LogEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='worklogentry_set')
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'))
    log_message = models.CharField(_('log_message'), max_length=512)

    class Meta:
        verbose_name = _(u'log entry')
        verbose_name_plural = _(u'log entries')
        ordering = ('-end', '-start')