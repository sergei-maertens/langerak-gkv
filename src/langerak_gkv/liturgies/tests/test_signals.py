from datetime import date, time

from django.test import TestCase

from .factories import LiturgyFactory
from langerak_gkv.activities.models import Activity


class SignalTests(TestCase):

    def test_activity_created(self):
        """
        Test that an activity is created when a liturgy is created.
        """
        liturgy = LiturgyFactory.create()
        activities = liturgy.activity_set.all()
        self.assertEqual(activities.count(), 1)

        activity = activities.first()
        self.assertEqual(activity.start_date, liturgy.date)
        self.assertEqual(activity.start_time, liturgy.service.time)
        self.assertEqual(activity.end_date, liturgy.date)

    def test_activity_updated(self):
        """
        Test that the linked activity date is updated if the liturgy changes.
        """
        liturgy = LiturgyFactory.create(date=date(2015, 2, 21), service__time=time(9, 30))
        liturgy.date = date(2015, 2, 22)
        liturgy.save()

        activity = liturgy.activity_set.first()
        self.assertEqual(activity.start_date, date(2015, 2, 22))
        self.assertEqual(activity.end_date, date(2015, 2, 22))

        liturgy.service.time = time(14, 0)
        liturgy.service.save()

        # refresh
        activity = activity.__class__.objects.get(pk=activity.pk)
        self.assertEqual(activity.start_time, time(14, 0))

    def test_activity_deleted(self):
        """
        Test that the activity is deleted if the liturgy is deleted
        """
        liturgy = LiturgyFactory.create(date=date(2015, 2, 21), service__time=time(9, 30))
        l_id = liturgy.id
        liturgy.delete()
        self.assertEqual(Activity.objects.filter(liturgy_id=l_id).count(), 0)
