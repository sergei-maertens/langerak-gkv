from django.test import RequestFactory, TestCase

from ..views import LoginModalView


class UserSearchTests(TestCase):
    factory = RequestFactory()

    def test_fetch_login_form_modal_content(self):
        request = self.factory.get("/foo")

        response = LoginModalView.as_view()(request)

        self.assertEqual(response.status_code, 200)
