import urllib
from datetime import date, datetime, time

from django.db.models import Q
from django.views.generic import (
    DayArchiveView, TemplateView, DetailView, WeekArchiveView, ListView
)

from django_ical.views import ICalFeed

from .models import Activity


class ActivitiesTodayMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ActivitiesTodayMixin, self).get_context_data(**kwargs)
        today = date.today()
        context['activities_today'] = Activity.objects.filter(
            Q(start_date=today) | Q(start_date__lt=today, end_date__gte=today)
        )
        today = date.today()
        context.update({
            'today': today,
            'this_week': today.strftime('%W'),
            'this_year': today.year
        })
        return context


class ActivityCalendarView(ActivitiesTodayMixin, TemplateView):
    template_name = 'activities/base.html'


class ActivityDetailView(ActivitiesTodayMixin, DetailView):
    model = Activity
    context_object_name = 'activity'


class ActivityWeekArchiveView(ActivitiesTodayMixin, WeekArchiveView):
    model = Activity
    date_field = 'start_date'
    context_object_name = 'activities'
    allow_future = True
    allow_empty = True


class ActivityDayArchiveView(ActivitiesTodayMixin, DayArchiveView):
    model = Activity
    date_field = 'start_date'
    context_object_name = 'activities'
    allow_future = True
    allow_empty = True
    month_format = '%m'


class ActivitySearchView(ActivitiesTodayMixin, ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = 'activities/searchresults.html'
    paginate_by = 50

    def get_queryset(self):
        terms = self.request.GET.get('q').split()
        q = Q()
        for term in terms:
            q |= Q(name__icontains=term) | Q(description__icontains=term) | \
                 Q(liturgy__preacher__icontains=term) | Q(liturgy__liturgy__icontains=term) | \
                 Q(liturgy__service_theme__icontains=term)
        return Activity.objects.filter(q).distinct()

    def get_context_data(self, **kwargs):
        context = super(ActivitySearchView, self).get_context_data(**kwargs)
        context['qs'] = urllib.urlencode({'q': self.request.GET.get('q')})
        return context


class Feed(ICalFeed):
    product_id = '-//koningskerk.nu//Activities//NL'
    timezone = 'Europe/Amsterdam'
    file_name = 'activities.ics'

    def items(self):
        return Activity.objects.all().order_by('-start_date', '-start_time', 'end_date')

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
