from datetime import datetime, time

from django.db.models import Q
from django.utils import timezone
from django.utils.http import urlencode
from django.views.generic import (
    CreateView,
    DayArchiveView,
    DetailView,
    ListView,
    TemplateView,
    WeekArchiveView,
)

from django_ical.views import ICalFeed

from langerak_gkv.utils.view_mixins import PermissionRequiredMixin

from .models import Activity


class ActivityCalendarView(TemplateView):
    template_name = "activities/base.html"


class ActivityDetailView(DetailView):
    model = Activity
    context_object_name = "activity"

    def get_context_data(self, **kwargs):
        context = super(ActivityDetailView, self).get_context_data(**kwargs)
        context["activity_pk"] = self.object.pk
        return context


class ActivityWeekArchiveView(WeekArchiveView):
    model = Activity
    date_field = "start_date"
    context_object_name = "activities"
    allow_future = True
    allow_empty = True


class ActivityDayArchiveView(DayArchiveView):
    model = Activity
    date_field = "start_date"
    context_object_name = "activities"
    allow_future = True
    allow_empty = True
    month_format = "%m"


class ActivitySearchView(ListView):
    model = Activity
    context_object_name = "activities"
    template_name = "activities/searchresults.html"
    paginate_by = 50

    def get_queryset(self):
        terms = self.request.GET.get("q", "").split()
        q = Q()
        for term in terms:
            q |= (
                Q(name__icontains=term)
                | Q(description__icontains=term)
                | Q(liturgy__preacher__icontains=term)
                | Q(liturgy__liturgy__icontains=term)
                | Q(liturgy__service_theme__icontains=term)
            )
        return Activity.objects.filter(q).distinct()

    def get_context_data(self, **kwargs):
        context = super(ActivitySearchView, self).get_context_data(**kwargs)
        context["qs"] = urlencode({"q": self.request.GET.get("q") or ""})
        return context


class ActivityCreateView(PermissionRequiredMixin, CreateView):
    model = Activity
    permissions = "activities.add_activity"
    fields = (
        "name",
        "type",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "location",
        "intended_public",
        "image",
        "description",
        "show_on_homepage",
        "url",
        "fb_event_id",
    )


class Feed(ICalFeed):
    product_id = "-//koningskerk.nu//Activities//NL"
    timezone = "Europe/Amsterdam"
    file_name = "activities.ics"

    def get_object(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return Activity.objects.get(pk=kwargs["pk"])
        return None

    def items(self, obj):
        queryset = Activity.objects.order_by("-start_date", "-start_time", "end_date")
        if obj:
            return queryset.filter(pk=obj.pk)
        return queryset.filter(start_date__gte=timezone.now())

    def item_link(self, item):
        return item.get_absolute_url()

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return datetime.combine(item.start_date, item.start_time or time())

    def item_end_datetime(self, item):
        return datetime.combine(item.end_date, item.end_time or time())
