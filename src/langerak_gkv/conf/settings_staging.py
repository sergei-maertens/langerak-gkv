from settings import *

#
# Standard Django settings.
#

DEBUG = False
TEMPLATE_DEBUG = DEBUG
WSGI_APPLICATION = 'langerak_gkv.wsgi.wsgi_staging.application'

ADMINS = (
    ('Sergei Maertens', 'sergeimaertens@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['langerak.gkv.nl']

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})


INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': 'http://',
    'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}


LOGIN_REDIRECT_URL = '/staging/'
MEDIA_URL = '/staging/media/'
STATIC_URL = '/staging/static/'

try:
    from .settings_local import *
except ImportError:
    pass
