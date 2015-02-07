from django.views.generic import TemplateView, DetailView

from .models import Activity


class ActivityCalendarView(TemplateView):
    template_name = 'activities/base.html'


class ActivityDetailView(DetailView):
    model = Activity
    context_object_name = 'activity'
