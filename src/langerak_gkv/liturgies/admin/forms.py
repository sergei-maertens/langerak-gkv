from django import forms
from django.core.mail import send_mail

import html2text

from langerak_gkv.mailing.forms import MailForm

from ..models import Liturgy, MailRecipient


class LiturgyMailForm(MailForm):
    recipients = forms.ModelMultipleChoiceField(queryset=MailRecipient.objects.none())
    is_html = forms.BooleanField(required=False, initial=False)

    class Meta(MailForm.Meta):
        fields = ("recipients", "subject", "body")
        widgets = {"body": forms.Textarea(attrs={"cols": 120, "rows": 20})}

    def __init__(self, *args, **kwargs):
        liturgies = kwargs.pop("liturgies")
        super(LiturgyMailForm, self).__init__(*args, **kwargs)
        self.fields["recipients"].queryset = MailRecipient.objects.filter(
            liturgy__in=liturgies, is_sent=False  # can only send once
        )

    def save(self, *args, **kwargs):
        mail = super(LiturgyMailForm, self).save(*args, **kwargs)

        body, html_message = mail.body, None
        if self.cleaned_data["is_html"]:
            html_message = mail.body
            body = html2text.html2text(html_message)

        recipients = self.cleaned_data["recipients"]
        to = [r.email for r in recipients]
        send_mail(mail.subject, body, None, to, html_message=html_message)
        recipients.update(is_sent=True)
        return mail


class LiturgiesForm(forms.Form):
    liturgy = forms.ModelMultipleChoiceField(queryset=Liturgy.objects.all())
