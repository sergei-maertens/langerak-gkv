from django.db import models
from django.template import Context, Template
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_text_ckeditor.fields import HTMLField
from djchoices import ChoiceItem, DjangoChoices

from .mail_template import Variable, validate_template


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


class Templates(DjangoChoices):
    liturgy = ChoiceItem('liturgy', _('Liturgy'))


@python_2_unicode_compatible
class MailTemplate(models.Model):
    template_type = models.CharField(_('type'), max_length=50, choices=Templates.choices, unique=True)

    subject = models.CharField(_('subject'), max_length=255)
    body = HTMLField(_('body'), help_text=_('Add the body with {{variable}} placeholders'))

    CONFIG = {
        Templates.liturgy: {
            'subject': [
                Variable('extra_churches'),
                Variable('datetime'),
            ],
            'body': [
                Variable('extra_churches'),
                Variable('day'),
                Variable('part_of_day'),
                Variable('liturgy_details', required=True)
            ]
        }
    }

    class Meta:
        verbose_name = _('mail template')
        verbose_name_plural = _('mail templates')

    def __str__(self):
        return self.template_type

    def clean(self):
        validate_template(self)

    def render(self, context):
        tpl_subject = Template(self.subject)
        tpl_body = Template(self.body)
        ctx = Context(context)
        return tpl_subject.render(ctx), tpl_body.render(ctx)
