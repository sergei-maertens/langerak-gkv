import raven
from .settings import *


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['koningskerk.nu', 'www.koningskerk.nu', 'live.koningskerk.nu']

LOGGING['loggers'].update({
    'langerak_gkv': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})

from .local import *  # noqa

#
# Raven
#
INSTALLED_APPS = list(INSTALLED_APPS) + [
    'raven.contrib.django.raven_compat',
]
RAVEN_CONFIG = {
    'dsn': RAVEN_DSN,
    'release': raven.fetch_git_sha(ROOT_DIR),
}
