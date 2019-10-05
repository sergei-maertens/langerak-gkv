from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

from langerak_gkv.mailing.models import Mail

from ..models import MailRecipient
from .forms import LiturgiesForm, LiturgyMailForm


class LiturgyEmailView(CreateView):
    model = Mail
    form_class = LiturgyMailForm
    template_name = "admin/liturgies/mail.html"
    success_url = reverse_lazy("admin:liturgies_liturgy_changelist")

    def _get_liturgies(self):
        form = LiturgiesForm(data=self.request.REQUEST)
        if form.is_valid():
            return form.cleaned_data["liturgy"]
        return []

    def get_initial(self):
        initial = super(LiturgyEmailView, self).get_initial()
        pks = self.request.GET.getlist("pk")
        if pks:
            liturgies = self._get_liturgies()
            initial["recipients"] = MailRecipient.objects.filter(pk__in=pks)
            initial["body"] = render_to_string(
                "liturgies/mail.html", {"liturgies": liturgies}
            )
            initial["subject"] = "Liturgie kerkdienst"
        return initial

    def get_form_kwargs(self):
        kwargs = super(LiturgyEmailView, self).get_form_kwargs()
        kwargs["liturgies"] = self._get_liturgies()
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs["opts"] = MailRecipient._meta
        kwargs["app_label"] = MailRecipient._meta.app_label
        kwargs["liturgies"] = self._get_liturgies()
        return super(LiturgyEmailView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        response = super(LiturgyEmailView, self).form_valid(form)
        messages.success(
            self.request,
            _("The email has been put on the queue and will be send shortly"),
        )
        return response
