from django import forms

from langerak_gkv.mailing.forms import MailForm
from ..models import MailRecipient


class LiturgyMailForm(MailForm):
    recipients = forms.ModelMultipleChoiceField(queryset=MailRecipient.objects.filter())

    def __init__(self, *args, **kwargs):
        liturgies = kwargs.pop('liturgies')
        super(LiturgyMailForm, self).__init__(*args, **kwargs)
        self.fields['recipients'].queryset = MailRecipient.objects.filter(
            liturgy__in=liturgies,
            is_sent=False  # can only send once
        )
