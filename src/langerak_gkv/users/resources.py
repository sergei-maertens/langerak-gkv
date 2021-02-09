from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import District, Family, User


class UserResource(resources.ModelResource):
    district = fields.Field(
        column_name="wijk",
        attribute="district",
        widget=ForeignKeyWidget(District, "name"),
    )

    class Meta:
        model = User
        import_id_fields = ("username",)
        fields = (
            "external_code",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "sex",
            "address",
            "postal_code",
            "city",
            "phone",
            "mobile",
            "birthdate",
            "district",
        )

    def before_import_row(self, row, **kwargs):
        if not row["email"]:
            row["email"] = "{}@koningskerk.nu".format(row["external_code"])

        if not row["username"] and row["email"]:
            # check if we can find the user
            try:
                username = User.objects.get(email=row["email"]).username
                row["username"] = username
            except User.DoesNotExist:
                row["username"] = row["email"]

    def before_save_instance(self, instance, using_transactions, dry_run):
        # find the family
        kwargs = {"address": instance.address, "postal_code": instance.postal_code}
        defaults = {"city": instance.city, "name": instance.last_name}
        family, created = Family.objects.get_or_create(defaults=defaults, **kwargs)
        instance.family = family
