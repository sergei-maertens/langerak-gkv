from datetime import date, time, timedelta

from django.test import TestCase

from ..models import Activity
from .factories import ActivityFactory


class UpcomingActivitiesTests(TestCase):
    def test_ordering_same_date(self):
        next_week = date.today() + timedelta(days=7)
        ActivityFactory.create(
            start_date=next_week,
            start_time=time(10, 0),
        )
        ActivityFactory.create(
            start_date=next_week,
            start_time=time(14, 0),
        )
        ActivityFactory.create(
            start_date=next_week,
            start_time=time(12, 0),
        )

        upcoming = Activity.objects.upcoming(n=3)

        self.assertQuerySetEqual(
            upcoming,
            [time(10, 0), time(12, 0), time(14, 0)],
            transform=lambda a: a.start_time,
        )

    def test_ordering_no_start_time(self):
        next_week = date.today() + timedelta(days=7)
        ActivityFactory.create(start_date=next_week, start_time=time(10, 0))
        ActivityFactory.create(start_date=next_week, start_time=None)

        upcoming = Activity.objects.upcoming()

        self.assertQuerySetEqual(
            upcoming,
            [None, time(10, 0)],
            transform=lambda a: a.start_time,
        )
