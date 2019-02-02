from datetime import date

from rest_framework import fields, serializers

from ..models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    title = fields.CharField(source='name')
    start = fields.DateTimeField(read_only=True)
    end = fields.DateTimeField(read_only=True)
    url = fields.URLField(source='get_absolute_url', read_only=True)
    textColor = fields.SerializerMethodField('get_text_color')

    class Meta:
        model = Activity
        fields = ('title', 'type', 'start', 'end', 'location', 'description',
                  'url', 'fb_event_id', 'textColor')

    def get_text_color(self, obj):
        if obj.start_date == date.today():
            return '#FFFFFF'
        return ''
