from django.db import models
from django.utils.translation import gettext_lazy as _


class Sex(models.TextChoices):
    male = "male", _("male")
    female = "female", _("female")
