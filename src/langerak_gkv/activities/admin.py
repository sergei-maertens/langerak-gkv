from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Activity, ActivityType, IntendedPublic


@admin.register(Activity)
class ActivityAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ("name", "start_date", "start_time", "end_date", "end_time")
    list_filter = ("start_date", "end_date", "type")
    search_fields = ("name", "description", "location")


admin.site.register(ActivityType)
admin.site.register(IntendedPublic)
