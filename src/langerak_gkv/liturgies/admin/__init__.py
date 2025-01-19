from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportActionModelAdmin

from ..models import Church, Liturgy, Service
from .resources import LiturgyResource


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ["name", "auto_selected"]


@admin.register(Liturgy)
class LiturgyAdmin(ImportExportActionModelAdmin):
    list_display = ("__str__", "date", "preacher")
    list_editable = ("preacher",)
    list_filter = ("date", "service__time")
    ordering = ("-date",)
    resource_class = LiturgyResource
    filter_horizontal = ("other_churches",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by("service__time")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "time")
    list_editable = ("name", "time")
    list_filter = ("time",)
    search_fields = ("name", "time")
