from django.contrib import admin
from .models import Liturgy, Service, MailRecipient


class MailRecipientInline(admin.TabularInline):
    model = MailRecipient
    can_delete = False


class LiturgyAdmin(admin.ModelAdmin):
    inlines = [MailRecipientInline]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'time')
    list_editable = ('name', 'time')
    list_filter = ('time',)
    search_fields = ('name', 'time')


admin.site.register(Liturgy, LiturgyAdmin)
admin.site.register(Service, ServiceAdmin)
