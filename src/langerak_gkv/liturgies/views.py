from django.views.generic import DetailView, ListView

from langerak_gkv.activities.views import ActivitiesTodayMixin
from .models import Liturgy


class LiturgyListView(ActivitiesTodayMixin, ListView):
    model = Liturgy
    template_name = 'liturgies/list.html'


class LiturgyDetailView(ActivitiesTodayMixin, DetailView):
    model = Liturgy
    template_name = 'liturgies/detail.html'
