from datetime import date

from django.views.generic import (
    ArchiveIndexView,
    DateDetailView,
    ListView,
    MonthArchiveView,
)

from langerak_gkv.activities.views import ActivitiesTodayMixin

from .models import Liturgy


class LiturgyListView(ActivitiesTodayMixin, ListView):
    model = Liturgy
    template_name = "liturgies/list.html"
    context_object_name = "liturgies"
    paginate_by = 10

    def get_queryset(self):
        qs = super(LiturgyListView, self).get_queryset()
        return qs.filter(date__gte=date.today()).order_by("date", "service__time")


class LiturgyArchiveView(ActivitiesTodayMixin, ArchiveIndexView):
    model = Liturgy
    date_field = "date"
    date_list_period = "month"


class LiturgyMonthArchiveView(ActivitiesTodayMixin, MonthArchiveView):
    queryset = Liturgy.objects.select_related("service").all()
    date_field = "date"
    month_format = "%m"
    context_object_name = "liturgies"
    allow_future = True


class LiturgyDateDetailView(ActivitiesTodayMixin, DateDetailView):
    queryset = Liturgy.objects.select_related("service").all()
    template_name = "liturgies/detail.html"
    allow_future = True
    date_field = "date"
    month_format = "%m"

    def get_context_data(self, **kwargs):
        kwargs["activity_pk"] = self.object.activity_set.first().pk
        return super(LiturgyDateDetailView, self).get_context_data(**kwargs)
