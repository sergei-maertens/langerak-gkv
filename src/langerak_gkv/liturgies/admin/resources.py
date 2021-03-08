from django.utils.dateparse import parse_time
from django.utils.translation import ugettext_lazy as _

from import_export import resources

from ..models import Liturgy, Service


class LiturgyResource(resources.ModelResource):
    class Meta:
        model = Liturgy
        fields = (
            "id",
            "date",
            "service__name",
            "service__time",
            "preacher",
            "preach_author",
            "bible_readings",
            "service_theme",
            "liturgy",
            "beamist",
            "organist",
            "collection_goal1",
            "collection_goal2",
            "collection_goal3",
            "extra_information",
        )

    def get_or_init_instance(self, instance_loader, row):
        instance, create = super(LiturgyResource, self).get_or_init_instance(
            instance_loader, row
        )

        # get_or_create the service
        name, time = row.get("service__name"), row.get("service__time")
        try:
            time = parse_time(time)
        except (TypeError, ValueError):
            raise ValueError(
                _(
                    "Could not parse time %s. Make sure that the "
                    "`service__time` field is formatted as text."
                )
                % time
            )
        instance.service, created = Service.objects.get_or_create(name=name, time=time)
        return instance, create
