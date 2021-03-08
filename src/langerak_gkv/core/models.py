from django.db import models
from django.utils.translation import gettext_lazy as _

from solo.models import SingletonModel


class SiteConfig(SingletonModel):
    gtm_code = models.CharField(
        _("Google Tag Manager code"),
        max_length=50,
        blank=True,
        help_text=_(
            "Typically looks like 'GTM-XXXX'. Supplying this installs Google Tag Manager."
        ),
    )
    analytics_code = models.CharField(
        _("Google Analytics code"),
        max_length=50,
        blank=True,
        help_text=_(
            "Typically looks like 'UA-XXXXX-Y'. Supplying this installs Google Analytics."
        ),
    )

    kerkdienst_gemist = models.URLField(
        _("'kerkdienst gemist' link"),
        blank=True,
    )
    youtube_channel = models.URLField(
        _("youtube kanaal"),
        blank=True,
    )
