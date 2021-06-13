from datetime import timedelta

import factory


class ActivityTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "activity type {n}".format(n=n))

    class Meta:
        model = "activities.ActivityType"


class ActivityFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("bs")
    start_date = factory.Faker("date_this_month")
    end_date = factory.LazyAttribute(lambda o: o.start_date + timedelta(days=3))

    type = factory.SubFactory(ActivityTypeFactory)
    description = factory.Faker("paragraph")

    class Meta:
        model = "activities.Activity"
