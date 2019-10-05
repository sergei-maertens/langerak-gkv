from django.core.exceptions import ValidationError
from django.urls import NoReverseMatch, reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class URLConfMenuEntry(models.Model):
    app_name = models.CharField(_('app name'), max_length=50)
    name = models.CharField(_('url name'), max_length=50)
    display_name = models.CharField(_('display name'), max_length=100)
    namespace = models.CharField(_('url namespace'), max_length=50, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _('urlconf menu entry')
        verbose_name_plural = _('urlconf menu entries')

    def __unicode__(self):
        if self.namespace:
            return u'{}:{}'.format(self.namespace, self.name)
        return self.name

    def clean(self):
        try:
            reverse(self.__unicode__())
        except NoReverseMatch:
            raise ValidationError(
                'URL <{}> could not be reversed.'.format(self.__unicode__())
            )

    def resolve(self):
        return reverse(self.__unicode__())
