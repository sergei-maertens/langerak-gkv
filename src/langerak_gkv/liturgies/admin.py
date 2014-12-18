from django.contrib import admin
from .models import Liturgy, Service, MailRecipient


class MailRecipientInline(admin.TabularInline):
    model = MailRecipient
    can_delete = False



class LiturgyAdmin(admin.ModelAdmin):
    inlines = [MailRecipientInline]

#         list_display = ('',)
#         list_filter = ('',)
#         inlines = [
#             Inline,
#         ]
#         raw_id_fields = ('',)
#         readonly_fields = ('',)
#         search_fields = ['']

admin.site.register(Liturgy, LiturgyAdmin)
admin.site.register(Service)
