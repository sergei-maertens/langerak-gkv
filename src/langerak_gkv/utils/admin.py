from django.contrib import admin

from .models import URLConfMenuEntry


class URLConfMenuEntryAdmin(admin.ModelAdmin):
    list_display = ("app_name", "__unicode__", "resolve")
    list_filter = ("app_name",)


admin.site.register(URLConfMenuEntry, URLConfMenuEntryAdmin)
