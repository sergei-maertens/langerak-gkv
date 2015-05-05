from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Society


class SocietyAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'member_count')
    filter_horizontal = ('members',)

    def get_queryset(self, request):
        qs = super(SocietyAdmin, self).get_queryset(request)
        return qs.prefetch_related('members')

    def member_count(self, obj):
        return obj.members.count()
    member_count.short_description = _('member count')


admin.site.register(Society, SocietyAdmin)
