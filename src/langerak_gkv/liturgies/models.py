from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djchoices import DjangoChoices, ChoiceItem


class Liturgy(models.Model):
    date = models.DateField(_('date'))
    service = models.ForeignKey('Service', verbose_name=_('service'))
    preacher = models.CharField(_('preacher'), max_length=100)
    preach_author = models.CharField(_('preach author'), max_length=100)
    main_section = models.CharField(_('main section'), max_length=50, blank=True)
    main_chapter = models.CharField(_('main chapter'), max_length=50, blank=True)
    main_verse = models.CharField(_('main verse'), max_length=50, blank=True)
    service_theme = models.CharField(_('service theme'), max_length=150, blank=True)
    liturgy = models.TextField(_('liturgy'))
    audiofile = models.FileField(_('audiofile'), upload_to='liturgies/audio', max_length=100, blank=True)
    beamist = models.CharField(_('beamist'), max_length=50, blank=True)  # search on function: beamists
    organist = models.CharField(_('organist'), max_length=50, blank=True)  # searches on function: organists
    collection_goal1 = models.CharField(_('collection goal 1'), max_length=50, blank=True)
    collection_goal2 = models.CharField(_('collection goal 2'), max_length=50, blank=True)
    collection_goal3 = models.CharField(_('collection goal 3'), max_length=50, blank=True)
    extra_information = models.TextField(_('extra information'), blank=True)

    class Meta:
        verbose_name = _('liturgy')
        verbose_name_plural = _('liturgies')
        ordering = ['date']

    def __unicode__(self):
        return u'{service} {date}'.format(
            service=self.service.name,
            date=self.date.strftime('%d-%m-%Y')
            )

    def get_absolute_url(self):
        return reverse('liturgies:archive_date_detail', kwargs={
            'year': self.date.year,
            'month': self.date.month,
            'day': self.date.day,
            'pk': self.pk
        })

    def get_collections(self):
        collections = []
        if self.collection_goal1:
            collections.append(self.collection_goal1)
        if self.collection_goal2:
            collections.append(self.collection_goal2)
        if self.collection_goal3:
            collections.append(self.collection_goal3)
        return collections


class Service(models.Model):
    name = models.CharField(_('service name'), max_length=50)
    time = models.TimeField(_('service time'))

    def __unicode__(self):
        return self.name


class MailRecipient(models.Model):

    class Functions(DjangoChoices):
        preacher = ChoiceItem('0preacher', _('preacher'))
        organist = ChoiceItem('1organist', _('organist'))
        beamist = ChoiceItem('2beamist', _('beamist'))
        other = ChoiceItem('3other', _('other'))

    liturgy = models.ForeignKey('Liturgy', verbose_name=_('liturgy'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254)
    function = models.CharField(choices=Functions.choices, max_length=10,
                                validators=[Functions.validator], blank=True)
    is_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['function']
