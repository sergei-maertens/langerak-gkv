from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

from .forms import PrayerOnDemandForm
from .models import PrayerOnDemand


class PODCreateView(CreateView):
    template_name = "homepage/home.html"
    model = PrayerOnDemand
    form_class = PrayerOnDemandForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(PODCreateView, self).get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs

    def form_valid(self, form):
        response = super(PODCreateView, self).form_valid(form)
        messages.success(
            self.request, _("Your request was received, we will pray for you.")
        )
        self.send_notification()
        return response

    def get_context_data(self, **kwargs):
        context = super(PODCreateView, self).get_context_data(**kwargs)
        context["pod_form"] = context["form"]
        return context

    def send_notification(self):
        path = reverse("admin:homepage_prayerondemand_change", args=[self.object.pk])
        uri = self.request.build_absolute_uri(location=path)
        msg = _(
            "A new 'Prayer on Demand' was submitted. You can view this " "at {uri}"
        ).format(uri=uri)
        send_mail(
            _("Prayer on demand"),
            msg,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_POD],
        )
