from unittest import skip
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django_webtest import WebTest

from ..models import PrayerOnDemand


class HomepageTests(WebTest):

    @skip('TODO')
    def test_homepage(self):
        # test that activities are on the homepage
        # test that the prayer on demand form is present
        pass

    def test_prayer_on_demand(self):
        """ Test that submitting the prayer on demand form sends an e-mail """
        homepage = self.app.get(reverse('pod'))
        self.assertEquals(homepage.status_code, 200)

        pod_form = homepage.forms[2]
        pod_form['email'] = 'test@test.com'
        pod_form['name'] = 'test name'
        pod_form['body'] = 'Pray for me'
        homepage = pod_form.submit().follow()

        qs = PrayerOnDemand.objects.all()
        self.assertEquals(qs.count(), 1)
        pod = qs.get()
        self.assertEquals(pod.email, 'test@test.com')
        self.assertEquals(pod.name, 'test name')
        self.assertEquals(pod.body, 'Pray for me')
        self.assertEquals(pod.replied, False)

        # test message
        self.assertContains(homepage, _('Your request was received, we will pray for you.'))

        # TODO: test that an e-mail was sent
