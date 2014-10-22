from django.views.generic import TemplateView

from .forms import PrayerOnDemandForm


class HomepageView(TemplateView):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        initial = {}
        if self.request.user.is_authenticated() and self.request.user.email:
            initial['email'] = self.request.user.email
        kwargs['form'] = PrayerOnDemandForm(initial=initial)

        return super(HomepageView, self).get_context_data(**kwargs)
