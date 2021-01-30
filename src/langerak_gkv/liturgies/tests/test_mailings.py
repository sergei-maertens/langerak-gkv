from django.core import mail
from django.urls import reverse

from django_webtest import WebTest

from langerak_gkv.users.tests.factories import UserFactory

from .factories import LiturgyFactory


class MailingTests(WebTest):
    def setUp(self):
        self.liturgies = LiturgyFactory.create_batch(
            2, preach_author="Jos den Homeros", liturgy="abcdefha;sljf"
        )
        self.user1 = UserFactory.create()
        self.superuser = UserFactory.create(is_staff=True, is_superuser=True)

    def test_admin_edit_email(self):
        url = reverse("admin:liturgies_liturgy_change", args=[self.liturgies[0].pk])
        changeform = self.app.get(url, user=self.superuser)
        changeform.form["mailrecipient_set-0-user"] = self.user1.pk

        response = changeform.form.submit().follow()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
