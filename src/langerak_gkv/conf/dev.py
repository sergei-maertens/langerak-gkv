import os

os.environ.setdefault('SECRET_KEY', 'development-secret-key')
os.environ.setdefault('ALLOWED_HOSTS', 'localhost,127.0.0.1')

os.environ.setdefault('DB_NAME', 'langerak_gkv')
os.environ.setdefault('DB_USER', 'langerak_gkv')
os.environ.setdefault('DB_PASSWORD', 'langerak_gkv')

from .base import *  # noqa, isort:skip

#
# Standard Django settings.
#

DEBUG = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING['loggers'].update({
    'langerak_gkv': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'performance': {
        'handlers': ['performance'],
        'level': 'INFO',
        'propagate': True,
    },
})

# Additional Django settings
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

DEFAULT_FROM_EMAIL = 'webmaster@localhost'

#
# Django debug toolbar
#
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'JQUERY_URL': None,
}

# Override settings with local settings.
try:
    from .local import *  # noqa
except ImportError:
    pass
