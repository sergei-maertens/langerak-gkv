from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Mail(models.Model):
    to = models.TextField()
    cc = models.TextField(blank=True)
    bcc = models.TextField(blank=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('emails')
        ordering = ('-pk',)

    def __str__(self):
        return self.subject
