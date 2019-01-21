import raven
from .base import *

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['langerak.gkv.nl', 'staging.koningskerk.nu']

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})


# INSTALLED_APPS += [
#     'raven.contrib.django.raven_compat',
# ]

RAVEN_CONFIG = {
    'dsn': 'http://',
    'release': raven.fetch_git_sha(ROOT_DIR),
}


try:
    from .local import *  # noqa
except ImportError:
    pass
