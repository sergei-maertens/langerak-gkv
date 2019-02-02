from __future__ import absolute_import

import os

os.environ['DB_NAME'] = 'koningskerk'
os.environ['DB_USER'] = 'postgres'
os.environ['ALLOWED_HOSTS'] = ''

from .base import *  # noqa, isort:skip

#
# Standard Django settings.
#

DEBUG = False

ADMINS = ()

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
