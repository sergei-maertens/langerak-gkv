from datetime import date

from django.views.generic import ListView, DateDetailView

from langerak_gkv.activities.views import ActivitiesTodayMixin
from .models import Liturgy


class LiturgyListView(ActivitiesTodayMixin, ListView):
    model = Liturgy
    template_name = 'liturgies/list.html'
    context_object_name = 'liturgies'
    paginate_by = 10

    def get_queryset(self):
        qs = super(LiturgyListView, self).get_queryset()
        return qs.filter(date__gte=date.today()).order_by('date')


class LiturgyDateDetailView(ActivitiesTodayMixin, DateDetailView):
    queryset = Liturgy.objects.select_related('service').all()
    template_name = 'liturgies/detail.html'
    allow_future = True
    date_field = 'date'
    month_format = '%m'
