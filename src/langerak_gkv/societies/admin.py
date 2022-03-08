from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Society


class SocietyAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ("name", "member_count", "edit_url")
    filter_horizontal = ("members",)

    def get_queryset(self, request):
        qs = super(SocietyAdmin, self).get_queryset(request)
        return qs.prefetch_related("members")

    def member_count(self, obj):
        return obj.members.count()

    member_count.short_description = _("member count")

    def edit_url(self, obj):
        url = obj.get_absolute_url()
        return '<a href="{}">{}</a>'.format(url, _("edit content"))

    edit_url.short_description = _("edit content")
    edit_url.allow_tags = True


admin.site.register(Society, SocietyAdmin)
