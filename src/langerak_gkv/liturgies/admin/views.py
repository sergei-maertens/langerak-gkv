from django.views.generic import CreateView

from langerak_gkv.mailing.models import Mail
from ..models import MailRecipient
from .forms import LiturgyMailForm


class LiturgyEmailView(CreateView):
    model = Mail
    form_class = LiturgyMailForm
    template_name = 'admin/liturgies/mail.html'

    def get_initial(self):
        initial = super(LiturgyEmailView, self).get_initial()
        pks = self.request.GET.getlist('pk')
        if pks:
            initial['recipients'] = MailRecipient.objects.filter(pk__in=pks)
        return initial

    def get_form_kwargs(self):
        kwargs = super(LiturgyEmailView, self).get_form_kwargs()
        liturgies = self.request.REQUEST.getlist('liturgies')
        kwargs['liturgies'] = liturgies
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['opts'] = MailRecipient._meta
        kwargs['app_label'] = MailRecipient._meta.app_label
        return super(LiturgyEmailView, self).get_context_data(**kwargs)
