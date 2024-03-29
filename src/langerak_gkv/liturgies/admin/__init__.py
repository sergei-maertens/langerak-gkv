from django.contrib import admin, messages
from django.template.defaultfilters import date, time
from django.template.loader import render_to_string
from django.urls import path, reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportActionModelAdmin

from langerak_gkv.mailing.models import MailTemplate, Templates

from ..models import Church, Liturgy, MailRecipient, Service
from .actions import send_liturgy_email
from .forms import LiturgyMailForm
from .resources import LiturgyResource
from .views import LiturgyEmailView


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MailRecipientInline(admin.TabularInline):
    model = MailRecipient
    can_delete = False


@admin.register(MailRecipient)
class MailRecipientAdmin(admin.ModelAdmin):
    list_display = ("liturgy", "email", "function", "user", "is_sent")
    list_filter = ("is_sent", "function")
    search_fields = (
        "liturgy__date",
        "liturgy__service__name",
        "liturgy__service_theme",
    )
    raw_id_fields = ("liturgy", "user")

    actions = [send_liturgy_email]

    def get_urls(self):
        """
        Hook in extra views.
        """
        urls = super(MailRecipientAdmin, self).get_urls()
        action_urls = [
            path(
                "send_mail/",
                self.admin_site.admin_view(LiturgyEmailView.as_view()),
                name="send_liturgy_email",
            )
        ]
        return action_urls + urls


@admin.register(Liturgy)
class LiturgyAdmin(ImportExportActionModelAdmin):
    list_display = ("__str__", "date", "preacher", "link_emails")
    list_editable = ("preacher",)
    list_filter = ("date", "service__time")
    ordering = ("-date",)
    inlines = [MailRecipientInline]
    resource_class = LiturgyResource
    filter_horizontal = ("other_churches",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by("service__time")

    def response_change(self, request, obj):
        """
        Also sent out the e-mails that aren't send yet.

        Hook in here because save_model doesn't save_related yet.
        """
        response = super(LiturgyAdmin, self).response_change(request, obj)

        recipients = MailRecipient.objects.filter(liturgy=obj, is_sent=False)
        if not recipients.exists():
            return response
        # send the unsent e-mails
        self._send_mail(obj, recipients)
        messages.success(
            request, _("The email has been put on the queue and will be send shortly")
        )
        return response

    def _send_mail(self, obj, recipients):
        subject = "Liturgie kerkdienst"
        body = render_to_string(
            "liturgies/mail.html", {"liturgies": [obj], "single": True}
        )
        template = MailTemplate.objects.filter(template_type=Templates.liturgy).first()
        if template is not None:
            extra_churches = ", ".join(
                list(obj.other_churches.values_list("name", flat=True))
            )
            subject, body = template.render(
                {
                    "extra_churches": "",
                    "day": date(obj.date, "l"),
                    "liturgy_details": mark_safe(body),
                    "extra_churches": "+ {}".format(extra_churches)
                    if extra_churches
                    else "",
                    "datetime": "{}, {}".format(
                        date(obj.date, "l j F"), time(obj.service.time, "H.i")
                    ),
                    "part_of_day": obj.part_of_day,
                }
            )

        initial = {
            "recipients": recipients,
            "body": body,
            "subject": subject,
            "is_html": True,
        }
        data = initial.copy()
        data["recipients"] = [r.id for r in recipients]
        form = LiturgyMailForm(liturgies=[obj], initial=initial, data=data)
        form.save()

    def link_emails(self, obj) -> str:
        url = reverse("admin:liturgies_mailrecipient_changelist")
        template = '<a href="{}?liturgy={}">{}</a>'
        return format_html(template, url, obj.pk, _("view email recipients"))

    link_emails.allow_tags = True


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "time")
    list_editable = ("name", "time")
    list_filter = ("time",)
    search_fields = ("name", "time")
