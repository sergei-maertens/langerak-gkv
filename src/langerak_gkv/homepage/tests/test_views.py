from django_webtest import WebTest

from unittest import skip


class HomepageTests(WebTest):

    @skip('TODO')
    def test_homepage(self):
        # test that activities are on the homepage
        # test that the prayer on demand form is present
        pass


    @skip('TODO')
    def test_prayer_on_demand(self):
        """ Test that submitting the prayer on demand form sends an e-mail """
