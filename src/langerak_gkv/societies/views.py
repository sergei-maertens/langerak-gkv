from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView

from .models import Society


class SocietyDetailView(DetailView):
    model = Society

    def get_queryset(self, **kwargs):
        if not self.request.user.is_superuser:
            return Society.objects.none()
        return super(SocietyDetailView, self).get_queryset(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        messages.warning(request, _("This page is only visible for content editors"))
        return super(SocietyDetailView, self).dispatch(request, *args, **kwargs)
