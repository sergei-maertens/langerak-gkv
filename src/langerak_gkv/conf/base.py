import os

from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices

# Automatically figure out the BASE_DIR and PROJECT_DIR.
DJANGO_PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
BASE_DIR = os.path.abspath(os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir))

#
# Standard Django settings.
#

DEBUG = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY')

ADMINS = (
    ('Sergei Maertens', 'sergeimaertens@gmail.com'),
)
MANAGERS = ADMINS

LANGUAGES = (
    ('nl', 'Nederlands'),
)
LANGUAGE_CODE = 'nl'

LOCALE_PATHS = (
    os.path.join(DJANGO_PROJECT_DIR, 'locale'),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', 5432),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'dummy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

SITE_ID = int(os.getenv('SITE_ID', '1'))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

FILE_UPLOAD_PERMISSIONS = 0644

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DJANGO_PROJECT_DIR, 'static'),

    # 3rd party NPM deps
    ('fullcalendar', os.path.join(BASE_DIR, 'node_modules', 'fullcalendar', 'dist')),
    ('momentjs', os.path.join(BASE_DIR, 'node_modules', 'moment', 'min')),
    ('jquery', os.path.join(BASE_DIR, 'node_modules', 'jquery', 'dist')),
    ('bootstrap', os.path.join(BASE_DIR, 'node_modules', 'bootstrap', 'dist')),
    ('font-awesome', os.path.join(BASE_DIR, 'node_modules', 'font-awesome')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DJANGO_PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',

                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

                'langerak_gkv.homepage.context_processors.sidebar',
                'langerak_gkv.users.context_processors.login',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # External middleware.
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    # 'axes.middleware.FailedLoginMiddleware'
]

ROOT_URLCONF = 'langerak_gkv.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'


FIXTURE_DIRS = (
    os.path.join(DJANGO_PROJECT_DIR, 'fixtures'),
)

INSTALLED_APPS = [
    # Note: contenttypes should be first, see Django ticket #10827
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',

    # order matters, needed for cms migrations
    'langerak_gkv.users',

    # External applications.
    'axes',
    'django_yubin',
    'compressor',
    'easy_thumbnails',
    'leaflet',
    'sniplates',
    'rest_framework',
    'rosetta',
    'haystack',
    'aldryn_search',
    # 'sorl.thumbnail',
    'newsletter',
    'import_export',
    'image_cropping',
    'password_reset',

    # cms
    'cms',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_video',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_video',
    'cmsplugin_filer_link',
    'menus',
    'sekizai',
    'djangocms_grid',

    # Project applications.
    'langerak_gkv.activities',
    'langerak_gkv.homepage',
    'langerak_gkv.liturgies',
    'langerak_gkv.mailing',
    'langerak_gkv.search',
    'langerak_gkv.societies',
    'langerak_gkv.utils',
    'langerak_gkv.worklog',
]

LOGGING_DIR = os.path.join(BASE_DIR, 'log')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(process)d %(thread)d  %(message)s'
        },
        'timestamped': {
            'format': '%(asctime)s %(levelname)s %(name)s  %(message)s'
        },
        'simple': {
            'format': '%(levelname)s  %(message)s'
        },
        'performance': {
            'format': '%(asctime)s %(process)d | %(thread)d | %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'timestamped'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),
            'formatter': 'verbose'
        },
        'project': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'langerak_gkv.log'),
            'formatter': 'verbose'
        },
        'performance': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'performance.log'),
            'formatter': 'performance'
        },
    },
    'loggers': {
        'langerak_gkv': {
            'handlers': ['project'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#
# Additional Django settings
# Enable these when using HTTPS
#

# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'

#
# Mailing
#
EMAIL_BACKEND = 'django_yubin.smtp_queue.EmailBackend'

#
# Django-axes
#
AXES_CACHE = 'dummy'
AXES_LOGIN_FAILURE_LIMIT = 3  # Default: 3
AXES_LOCK_OUT_AT_FAILURE = True  # Default: True
AXES_USE_USER_AGENT = False  # Default: False

#
# Auth
#

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'langerak_gkv.users.backends.UsernameModelBackend',
]
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = '/'


#
# Easy thumbnails
#
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_ALIASES = {
    '': {
        'default': {
            'size': (400, 300),
            'crop': True,
            'upscale': True,
        },
        'small': {
            'size': (120, 120),
            'crop': True,
            'upscale': True,
        },
        'avatar_portrait': {
            'size': (300, 300),
            'crop': True,
            'upscale': True,
        },
        'header': {
            'size': (1170, 315),
            'crop': True,
            'upscale': True,
        },
        'birthday': {
            'size': (50, 50),
            'crop': True,
            'upscale': True,
        },
        'activity_detail': {
            'size': (800, 400),
            'crop': True,
            'upscale': True,
        }
    }
}
THUMBNAIL_ALIASES['']['homepage'] = THUMBNAIL_ALIASES['']['default']

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
)

#
# Django CMS
#
CMS_PERMISSION = True

CMS_TEMPLATES = (
    ('cms/default.html', _('Default')),
    ('homepage/home.html', _('Homepage')),
    ('cms/right_sidebar.html', _('Content left, sidebar right')),
    ('cms/3_columns.html', _('3 Columns (responsive)')),
)

CMS_PLACEHOLDER_CONF = {
    'header_image': {
        'plugins': ['FilerImagePlugin'],
    },
    'slot1': {'plugins': ['HomepageLinkPlugin']},
    'slot2': {'plugins': ['HomepageLinkPlugin']},
    'slot3': {'plugins': ['HomepageLinkPlugin']},
    'slot4': {'plugins': ['HomepageLinkPlugin']},
    'preach_image': {'plugins': ['FilerImagePlugin']},
    'preach_title': {'plugins': ['CharFieldPlugin']},
    'preach_subtitle': {'plugins': ['CharFieldPlugin']},
}

CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('header', _('header top image')),
)

DJANGOCMS_GRID_CONFIG = {
    'COLUMNS': 12,
    'TOTAL_WIDTH': 1170,
    'GUTTER': 30,
}


class FilerStyles(DjangoChoices):
    default = ChoiceItem(' ', _('Default'))
    orange = ChoiceItem('orange', _('Orange'))
    blue = ChoiceItem('blue', _('Blue'))
    green = ChoiceItem('green', _('Green'))
    purple = ChoiceItem('purple', _('Purple'))
    orange_rm = ChoiceItem('orange read-more', _('Read-more orange'))
    blue_rm = ChoiceItem('blue read-more', _('Read-more blue'))
    green_rm = ChoiceItem('green read-more', _('Read-more green'))
    purple_rm = ChoiceItem('purple read-more', _('Read-more purple'))


FILER_LINK_STYLES = FilerStyles.choices


#
# GEO
#
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (51.93, 4.876),
    'DEFAULT_ZOOM': 9,
    # 'TILES': [(_('Streets'), 'http://openmapsurfer.uni-hd.de/tiles/roads/x={x}&y={y}&z={z}', {
    #     'minZoom': 0, 'maxZoom': 20, 'attribution': '',
    # })]
}

#
# EMAIL addresses
#
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_POD = 'pod@langerak.gkv.nl'
EMAIL_ORGANIST = 'organist@langerak.gkv.nl'
EMAIL_BEAMIST = 'beamist@langerak.gkv.nl'
EMAIL_KOSTER = 'koster@langerak.gkv.nl'
EMAIL_PREACHER = 'predikant@langerak.gkv.nl'
EMAIL_BIBLE_GROUP = 'bijbelleesgroep@langerak.gkv.nl'
EMAIL_PREACH_CREATION = 'preekvoorziening@langerak.gkv.nl'


#
# Django-haystack
#
HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'ENGINE': 'langerak_gkv.search.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'koningskerk',
    },
}

ELASTICSEARCH_INDEX_SETTINGS = {
    u'settings': {
        u'analysis': {
            u'filter': {
                u'haystack_edgengram': {
                    u'max_gram': 30,  # Default: 15. Make this larger to ensure long words are properly found
                    u'type': u'edgeNGram',
                    u'min_gram': 2  # Default: 2. Keep this small to ensure we get results for partial words
                },
                u'haystack_ngram': {
                    u'max_gram': 15,
                    u'type': u'nGram',
                    u'min_gram': 2  # Default: 3
                }
            },
            u'tokenizer': {
                u'haystack_edgengram_tokenizer': {
                    u'max_gram': 15,
                    u'type': u'edgeNGram',
                    # u'side': u'front',
                    u'min_gram': 2
                },
                u'haystack_ngram_tokenizer': {
                    u'max_gram': 15,
                    u'type': u'nGram',
                    u'min_gram': 2
                },
            },
            u'analyzer': {
                u'edgengram_analyzer': {
                    u'filter': [u'lowercase', u'haystack_edgengram'],
                    u'type': u'custom',
                    # Required for searching numbers:
                    # http://stackoverflow.com/questions/13636419/elasticsearch-edgengrams-and-numbers
                    u'tokenizer': u'standard'
                },
                u'ngram_analyzer': {
                    u'filter': [u'haystack_ngram'],
                    u'type': u'custom',
                    u'tokenizer': u'lowercase'
                }
            }
        }
    }
}

#
# DJANGO-IMPORT-EXPORT
#
IMPORT_EXPORT_USE_TRANSACTIONS = True

#
# IMAGE CROPPING
#
# IMAGE_CROPPING_JQUERY_URL = None  # we embed it ourselves
IMAGE_CROPPING_SIZE_WARNING = True


#
# Tests
#
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Raven
SENTRY_DSN = os.getenv('SENTRY_DSN')

if SENTRY_DSN:
    import raven

    INSTALLED_APPS = INSTALLED_APPS + [
        'raven.contrib.django.raven_compat',
    ]

    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
        'release': raven.fetch_git_sha(BASE_DIR),
    }
    LOGGING['handlers'].update({
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': RAVEN_CONFIG['dsn']
        },
    })
