from datetime import date

from django.db.models import Q
from django.views.generic import (
    DayArchiveView, TemplateView, DetailView, WeekArchiveView, ListView
)

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
    paginate_by = 4

    def get_queryset(self):
        term = self.request.GET.get('q')
        return Activity.objects.filter(name__icontains=term)