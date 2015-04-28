from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf.urls import patterns, url

from ..models import Liturgy, Service, MailRecipient
from .actions import send_liturgy_email
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


class LiturgyAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'preacher', 'link_emails')
    list_editable = ('preacher',)
    list_filter = ('date', 'service__time')
    inlines = [MailRecipientInline]

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
