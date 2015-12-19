from django.conf.urls import patterns, url
from django.contrib import admin, messages
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportActionModelAdmin

from ..models import Liturgy, Service, MailRecipient
from .actions import send_liturgy_email
from .forms import LiturgyMailForm
from .resources import LiturgyResource
from .views import LiturgyEmailView


class MailRecipientInline(admin.TabularInline):
    model = MailRecipient
    can_delete = False


class MailRecipientAdmin(admin.ModelAdmin):
    list_display = ('liturgy', 'email', 'function', 'user', 'is_sent')
    list_filter = ('is_sent', 'function')
    search_fields = ('liturgy__date', 'liturgy__service__name', 'liturgy__service_theme')
    raw_id_fields = ('liturgy', 'user')

    actions = [send_liturgy_email]

    def get_urls(self):
        """
        Hook in extra views.
        """
        urls = super(MailRecipientAdmin, self).get_urls()
        action_urls = patterns(
            '',
            url(
                r'^send_mail/$',
                self.admin_site.admin_view(LiturgyEmailView.as_view()),
                name='send_liturgy_email'
            ),
        )
        return action_urls + urls


class LiturgyAdmin(ImportExportActionModelAdmin):
    list_display = ('__unicode__', 'date', 'preacher', 'link_emails')
    list_editable = ('preacher',)
    list_filter = ('date', 'service__time')
    inlines = [MailRecipientInline]
    resource_class = LiturgyResource

    def response_change(self, request, obj):
        """
        Also sent out the e-mails that aren't send yet.

        Hook in here because save_model doesn't save_related yet.
        """
        response = super(LiturgyAdmin, self).response_change(request, obj)

        # send the unset e-mails
        recipients = MailRecipient.objects.filter(liturgy=obj, is_sent=False)
        if not recipients.exists():
            return response

        initial = {
            'recipients': recipients,
            'body': render_to_string('liturgies/mail.html', {'liturgies': [obj]}),
            'subject': 'Liturgie kerkdienst',
        }
        data = initial.copy()
        data['recipients'] = [r.id for r in recipients]
        form = LiturgyMailForm(liturgies=[obj], initial=initial, data=data)
        form.save()
        messages.success(request, _('The email has been put on the queue and will be send shortly'))
        return response

    def link_emails(self, obj):
        url = reverse('admin:liturgies_mailrecipient_changelist')
        return u'<a href="{}?liturgy={}">{}</a>'.format(url, obj.pk, _('view email recipients'))
    link_emails.allow_tags = True


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'time')
    list_editable = ('name', 'time')
    list_filter = ('time',)
    search_fields = ('name', 'time')


admin.site.register(Liturgy, LiturgyAdmin)
admin.site.register(MailRecipient, MailRecipientAdmin)
admin.site.register(Service, ServiceAdmin)
