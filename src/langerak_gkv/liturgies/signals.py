from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _

from langerak_gkv.activities.models import Activity, ActivityType
from .models import Liturgy, Service


@receiver(post_save, sender=Liturgy, dispatch_uid='sync_liturgy_activity')
def create_or_update_activity(sender, instance, created, **kwargs):

    if kwargs.get('raw'):
        return

    if created:
        act_type, __ = ActivityType.objects.get_or_create(name=_('liturgy'))
        Activity.objects.create(
            name=instance.service.name,
            start_date=instance.date,
            end_date=instance.date,
            start_time=instance.service.time,
            liturgy=instance,
            type=act_type
        )
    else:
        activities = instance.activity_set.exclude(start_date=instance.date, end_date=instance.date)
        activities.update(start_date=instance.date, end_date=instance.date)


@receiver(post_save, sender=Service, dispatch_uid='sync_service_activity')
def update_activity(sender, instance, created, **kwargs):
    if not created:  # only track updates
        Activity.objects.filter(
            liturgy__service=instance
        ).exclude(
            start_time=instance.time
        ).update(start_time=instance.time)
