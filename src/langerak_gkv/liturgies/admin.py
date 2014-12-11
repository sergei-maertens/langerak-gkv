from django.contrib import admin
from .models import Liturgy, Service

class LiturgyAdmin(admin.ModelAdmin):
    pass
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
