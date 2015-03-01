from django.views.generic import ListView, DateDetailView

from langerak_gkv.activities.views import ActivitiesTodayMixin
from .models import Liturgy


class LiturgyListView(ActivitiesTodayMixin, ListView):
    model = Liturgy
    template_name = 'liturgies/list.html'


class LiturgyDateDetailView(ActivitiesTodayMixin, DateDetailView):
    queryset = Liturgy.objects.select_related('service').all()
    template_name = 'liturgies/detail.html'
    allow_future = True
    date_field = 'date'
    month_format = '%m'
