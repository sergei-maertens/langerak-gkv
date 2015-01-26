from django.views.generic import TemplateView


class ActivityCalendarView(TemplateView):
    template_name = 'activities/base.html'
