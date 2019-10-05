from django.contrib import admin

from .models import PrayerOnDemand


class PrayerOnDemandAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "body", "replied")
    list_editable = ("replied",)
    search_fields = ("name", "email")
    list_filter = ("replied", "created", "modified")


admin.site.register(PrayerOnDemand, PrayerOnDemandAdmin)
