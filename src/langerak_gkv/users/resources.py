from datetime import date

from import_export import resources

from .models import Family, User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ("external_code",)
        fields = (
            "id",
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
        )

    def before_import(self, dataset, dry_run, **kwargs):
        header_index = dataset.headers.index
        day, month, year = (
            header_index("datum"),
            header_index("mnd"),
            header_index("jaar"),
        )

        if not any(dataset[0]):
            del dataset[0]

        def birthdate(row):
            try:
                bd = date(int(row[year]), int(row[month]), int(row[day]))
                return "{0:%Y-%m-%d}".format(bd)
            except ValueError:
                return None

        dataset.append_col(birthdate, header="birthdate")

        sex = header_index("voorvoegsel")

        def get_sex(row):
            if row[sex] == "dhr.":
                return User.Sex.male
            elif row[sex] == "mevr.":
                return User.Sex.female
            return ""

        dataset.append_col(get_sex, header="sex")

    def import_obj(self, obj, data, dry_run):
        super(UserResource, self).import_obj(obj, data, dry_run)
        if not obj.email:
            obj.email = "{}@koningskerk.nu".format(data["external_code"])

    def before_save_instance(self, instance, dry_run):
        if (
            self.get_queryset()
            .filter(email=instance.email)
            .exclude(pk=instance.pk)
            .exists()
        ):
            instance.email = "{}@koningskerk.nu".format(instance.external_code)

        # find the family
        kwargs = {"address": instance.address, "postal_code": instance.postal_code}
        defaults = {"city": instance.city, "name": instance.last_name}
        family, created = Family.objects.get_or_create(defaults=defaults, **kwargs)
        instance.family = family
