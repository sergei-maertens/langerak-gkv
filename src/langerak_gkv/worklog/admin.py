from django.contrib import admin

from .models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_spent', 'start', 'end', 'log_message', 'paid')
    list_editable = ('paid',)
    list_filter = ('user',)
    search_fields = ('user__first_name', 'user__last_name', 'log_message')

admin.site.register(LogEntry, LogEntryAdmin)