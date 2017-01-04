from datetime import time

from django.test import TestCase
from django.utils.translation import ugettext as _

from langerak_gkv.activities.models import Activity

from .factories import LiturgyFactory, ServiceFactory


class LiturgyTests(TestCase):

    def test_part_of_day(self):
        liturgy1 = LiturgyFactory.build(service__time=time(9, 30))
        liturgy2 = LiturgyFactory.build(service__time=time(11, 30))
        liturgy3 = LiturgyFactory.build(service__time=time(16, 00))
        liturgy4 = LiturgyFactory.build(service__time=time(17, 00))

        self.assertEqual(liturgy1.part_of_day, _('morning'))
        self.assertEqual(liturgy2.part_of_day, _('morning'))
        self.assertEqual(liturgy3.part_of_day, _('afternoon'))
        self.assertEqual(liturgy4.part_of_day, _('evening'))

    def test_updates_activity(self):
        liturgy = LiturgyFactory.create(service__time=time(16, 30))
        activity = Activity.objects.get()
        self.assertEqual(activity.start_time, time(16, 30))

        liturgy.service = ServiceFactory.create(time=time(18, 30))
        liturgy.save()
        activity.refresh_from_db()
        self.assertEqual(activity.start_time, time(18, 30))
