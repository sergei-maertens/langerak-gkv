import os

os.environ.setdefault("LOG_STDOUT", "yes")

from .base import *  # noqa

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LOGGING["loggers"].update(
    {
        "langerak_gkv": {
            "handlers": ["project"],
            "level": "WARNING",
            "propagate": True,
        },
        "django": {"handlers": ["django"], "level": "WARNING", "propagate": True},
    }
)

# The file storage engine to use when collecting static files with the
# collectstatic management command.
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
