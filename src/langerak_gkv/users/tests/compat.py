"""
Yikes

https://github.com/django-cms/django-cms/issues/7225
"""

from cms.models import PageUser

from ..models import User


class DeletePageUsersMixin:
    def tearDown(self):
        # multi-table inheritance seems to be causing problems...
        users = User.objects.all()
        PageUser.objects.filter(pk__in=users.values_list("pk", flat=True)).delete()

        super().tearDown()
