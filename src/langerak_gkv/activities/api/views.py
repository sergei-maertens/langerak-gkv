from rest_framework import generics

from ..models import Activity
from .serializers import ActivitySerializer
from .forms import CalendarRangeForm


class ActivityListApiView(generics.ListAPIView):
    model = Activity
    serializer_class = ActivitySerializer

    def get_queryset(self):
        base = super(ActivityListApiView, self).get_queryset()
        range_form = CalendarRangeForm(self.request.GET)
        if range_form.is_valid():
            qs = base.filter(
                start_date__lte=range_form.cleaned_data['end'],
                end_date__gte=range_form.cleaned_data['start']
            )
        else:
            qs = base
        return qs
