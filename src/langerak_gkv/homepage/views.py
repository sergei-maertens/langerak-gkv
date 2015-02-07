from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, CreateView

from langerak_gkv.activities.models import Activity

from .forms import PrayerOnDemandForm
from .models import PrayerOnDemand


class HomepageContextMixin(object):
    def get_context_data(self, **kwargs):
        # TODO: get the current/last preacher
        kwargs['preacher'] = 'ds H.J. Lopers'
        kwargs['upcoming_activities'] = Activity.objects.upcoming(n=5)
        return kwargs


class HomepageView(HomepageContextMixin, TemplateView):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        # form initialization is specific to this view, the create view has its
        # own form builder
        initial = {}
        if self.request.user.is_authenticated() and self.request.user.email:
            initial['email'] = self.request.user.email
        kwargs['form'] = PrayerOnDemandForm(initial=initial)
        kwargs['activities'] = Activity.objects.homepage().order_by('?')[:4]
        return super(HomepageView, self).get_context_data(**kwargs)


class PODCreateView(HomepageContextMixin, CreateView):
    template_name = 'homepage/home.html'
    model = PrayerOnDemand
    form_class = PrayerOnDemandForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super(PODCreateView, self).form_valid(form)
        messages.success(self.request, _('Your request was received, we will pray for you.'))
        # TODO: send e-mail
        return response
