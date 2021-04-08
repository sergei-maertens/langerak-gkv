import uuid

from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import District, Family, User


class GetOrCreateForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        try:
            value = super().clean(value, row=row, *args, **kwargs)
        except self.model.DoesNotExist:
            value = self.model._default_manager.create(**{self.field: value})
        return value


class UserResource(resources.ModelResource):
    phone = fields.Field(
        attribute="phone",
        saves_null_values=False,
    )
    mobile = fields.Field(
        attribute="mobile",
        saves_null_values=False,
    )
    district = fields.Field(
        column_name="wijk",
        attribute="district",
        widget=GetOrCreateForeignKeyWidget(District, "name"),
    )

    class Meta:
        model = User
        import_id_fields = ("username",)
        fields = (
            "username",
            "email",
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
            "external_code",
            "district",
        )
        export_order = fields

    def before_import_row(self, row, **kwargs):
        if not row["email"]:
            ext_code = row["external_code"]
            row["email"] = "{}@koningskerk.nu".format(ext_code) if ext_code else ""

        if not row["username"] and row["email"]:
            # check if we can find the user
            try:
                username = User.objects.get(email=row["email"]).username
                row["username"] = username
            except User.DoesNotExist:
                row["username"] = row["email"]

        elif not row["username"] and not row["email"]:
            row["username"] = str(uuid.uuid4())

    def before_save_instance(self, instance, using_transactions, dry_run):
        # find the family
        kwargs = {"address": instance.address, "postal_code": instance.postal_code}
        defaults = {"city": instance.city, "name": instance.last_name}
        family, created = Family.objects.get_or_create(defaults=defaults, **kwargs)
        instance.family = family
