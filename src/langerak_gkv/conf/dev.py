import os

os.environ.setdefault("SECRET_KEY", "development-secret-key")
os.environ.setdefault("ALLOWED_HOSTS", "localhost,127.0.0.1")

os.environ.setdefault("IS_HTTPS", "0")
os.environ.setdefault("DB_NAME", "langerak_gkv")
os.environ.setdefault("DB_USER", "langerak_gkv")
os.environ.setdefault("DB_PASSWORD", "langerak_gkv")

from .base import *  # noqa, isort:skip

#
# Standard Django settings.
#

DEBUG = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING["loggers"].update(
    {
        "langerak_gkv": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "performance": {
            "handlers": ["performance"],
            "level": "INFO",
            "propagate": True,
        },
    }
)

# Additional Django settings
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

DEFAULT_FROM_EMAIL = "webmaster@localhost"

#
# Django debug toolbar
#
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False, "JQUERY_URL": None}

INSTALLED_APPS += ["django_extensions"]

CMS_PAGE_CACHE = config("CMS_PAGE_CACHE", default=True)

# Override settings with local settings.
try:
    from .local import *  # noqa
except ImportError:
    pass
