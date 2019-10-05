from django.contrib import admin

from .models import MailTemplate


@admin.register(MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = ["template_type"]
    list_filter = ["template_type"]
