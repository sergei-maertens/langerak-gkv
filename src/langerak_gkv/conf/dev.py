from .base import *

#
# Standard Django settings.
#

DEBUG = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MANAGERS = ADMINS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite'),
        # The following settings are not used with sqlite3:
        'USER': 'langerak',
        'PASSWORD': 'langerak',
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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
