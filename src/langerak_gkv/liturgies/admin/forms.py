from django import forms

from langerak_gkv.mailing.forms import MailForm
from ..models import MailRecipient


class LiturgyMailForm(MailForm):
    recipients = forms.ModelMultipleChoiceField(queryset=MailRecipient.objects.filter())

    class Meta(MailForm.Meta):
        fields = ('recipients', 'subject', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'cols': 120, 'rows': 20})
        }

    def __init__(self, *args, **kwargs):
        liturgies = kwargs.pop('liturgies')
        super(LiturgyMailForm, self).__init__(*args, **kwargs)
        self.fields['recipients'].queryset = MailRecipient.objects.filter(
            liturgy__in=liturgies,
            is_sent=False  # can only send once
        )

    def save(self, *args, **kwargs):
        import bpdb; bpdb.set_trace()
