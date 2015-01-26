from rest_framework import serializers, fields

from ..models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    start = fields.DateTimeField(read_only=True)
    end = fields.DateTimeField(read_only=True)

    class Meta:
        model = Activity
        fields = (
            'name', 'type',
            'start', 'end',
            'location', 'description',
            'url', 'fb_event_id'
        )
