from datetime import date

from django.db.models import Q
from django.views.generic import TemplateView, DetailView, WeekArchiveView

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
