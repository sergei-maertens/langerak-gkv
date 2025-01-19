from datetime import date

from django.views.generic import (
    ArchiveIndexView,
    DateDetailView,
    ListView,
    MonthArchiveView,
)

from .models import Liturgy


class LiturgyListView(ListView):
    model = Liturgy
    template_name = "liturgies/list.html"
    context_object_name = "liturgies"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        return (
            qs.filter(date__gte=date.today())
            .prefetch_related("other_churches")
            .select_related("service")
            .order_by("date", "service__time")
        )


class LiturgyArchiveView(ArchiveIndexView):
    model = Liturgy
    date_field = "date"
    date_list_period = "month"


class LiturgyMonthArchiveView(MonthArchiveView):
    queryset = Liturgy.objects.select_related("service").all()
    date_field = "date"
    month_format = "%m"
    context_object_name = "liturgies"
    allow_future = True


class LiturgyDateDetailView(DateDetailView):
    queryset = Liturgy.objects.select_related("service").all()
    template_name = "liturgies/detail.html"
    allow_future = True
    date_field = "date"
    month_format = "%m"
