from datetime import date

from django.test import RequestFactory, TestCase

from freezegun import freeze_time

from ..views import UserSearchView
from .compat import DeletePageUsersMixin
from .factories import UserFactory


class UserSearchTests(DeletePageUsersMixin, TestCase):
    factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.user = UserFactory.create(exclude_in_queries=True)

    def assertSearchResults(self, params, expected):
        request = self.factory.get("/foo", params)
        request.user = self.user

        response = UserSearchView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context_data["profiles"],
            expected,
            transform=lambda x: x,
        )

    def test_search_by_partial_family_name(self):
        UserFactory.create(last_name="Verstappen")
        user2 = UserFactory.create(last_name="Hamilton")
        query = {"last_name": "Ham"}

        self.assertSearchResults(query, [user2])

    @freeze_time("2022-04-18T13:28:00Z")
    def test_filter_by_age(self):
        user1 = UserFactory.create(birthdate=date(1989, 1, 23))
        user2 = UserFactory.create(birthdate=date(1996, 12, 4))

        with self.subTest("minimum age"):
            query = {"min_age": 30}

            self.assertSearchResults(query, [user1])

        with self.subTest("maximum age"):
            query = {"max_age": 27}

            self.assertSearchResults(query, [user2])

    def test_filter_by_full_name_and_query(self):
        user1 = UserFactory.create(first_name="Damon", last_name="Hill")
        user2 = UserFactory.create(first_name="Lewis", last_name="Hamilton")
        user3 = UserFactory.create(
            first_name="Sebastian", last_name="Vettel", about_me="German"
        )

        with self.subTest("full name variations"):
            variations = ["lewis", "hamilton", "lewis ham", "lewis hamilton"]
            for variation in variations:
                with self.subTest(variation=variation):
                    query = {"full_name": variation}

                    self.assertSearchResults(query, [user2])

        with self.subTest("query variations, name"):
            variations = ["dam", "Hill", "damo hil"]
            for variation in variations:
                with self.subTest(variation=variation):
                    query = {"query": variation}

                    self.assertSearchResults(query, [user1])

        with self.subTest("query variations, about_me"):
            query = {"query": "germ"}

            self.assertSearchResults(query, [user3])

    def test_partial_matches_street_name(self):
        user = UserFactory.create(address="Dorpsplein 69")

        query = {"address": "dorpsplein"}

        self.assertSearchResults(query, [user])
