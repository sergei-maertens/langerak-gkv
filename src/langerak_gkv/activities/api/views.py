from rest_framework import generics

from ..models import Activity
from .serializers import ActivitySerializer


class ActivityListApiView(generics.ListAPIView):
    model = Activity
    serializer_class = ActivitySerializer

    def get_queryset(self):
        base = super(ActivityListApiView, self).get_queryset()
        return base
