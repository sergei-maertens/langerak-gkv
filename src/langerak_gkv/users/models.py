from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        constraints = (
            models.UniqueConstraint(
                fields=("email",), name="unique_email", condition=~models.Q(email="")
            ),
        )

    def __str__(self):
        full_name = self.get_full_name().strip()
        return full_name or getattr(self, self.USERNAME_FIELD)
