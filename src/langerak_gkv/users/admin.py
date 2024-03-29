from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportMixin

from .forms import UserChangeForm, UserCreationForm
from .models import District, DistrictFunction, Family, RelationType, User, UserRelation
from .resources import UserResource


class UserRelationInline(admin.TabularInline):
    model = UserRelation
    fk_name = "user1"
    raw_id_fields = ["user2"]


class UserAdmin(ImportExportMixin, _UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    ("first_name", "last_name"),
                    "sex",
                    "address",
                    ("postal_code", "city"),
                    ("phone", "mobile"),
                    "birthdate",
                    "picture",
                    "cropping",
                    "about_me",
                )
            },
        ),
        (
            _("Family and location"),
            {"fields": ("district",)},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "exclude_in_queries",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "date_joined"), "classes": ("collapse",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "district",
        "district_function",
    )
    list_filter = _UserAdmin.list_filter + (
        "district",
        "district_function",
        "family",
        "exclude_in_queries",
    )
    list_select_related = ("district",)
    search_fields = ("first_name", "last_name__icontains", "email", "username")
    ordering = ("email",)

    inlines = [UserRelationInline]
    resource_class = UserResource


class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class DistrictFunctionAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class RelationTypeAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "name_male",
        "name_female",
        "reverse_name_male",
        "reverse_name_female",
        "is_partner",
        "is_child_parent",
    )
    list_editable = list_display[1:]
    search_fields = list_display[1:-2]
    readonly_fields = ("reverse",)


class FamilyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "postal_code", "city")
    search_fields = ("name", "postal_code", "address")


admin.site.register(User, UserAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(DistrictFunction, DistrictFunctionAdmin)
admin.site.register(RelationType, RelationTypeAdmin)
