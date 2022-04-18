from django.test import RequestFactory, TestCase

from ..views import UserSearchView
from .factories import UserFactory


class UserSearchTests(TestCase):

    factory = RequestFactory()

    def test_search_by_partial_family_name(self):
        user1 = UserFactory.create(last_name="Verstappen")
        user2 = UserFactory.create(last_name="Hamilton")
        form_data = {"last_name": "Ham"}
        request = self.factory.get("/foo", form_data)
        request.user = user1

        response = UserSearchView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context_data["profiles"],
            [user2],
            transform=lambda x: x,
        )
