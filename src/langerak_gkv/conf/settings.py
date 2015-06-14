import os

import django.conf.global_settings as DEFAULT_SETTINGS
from django.utils.translation import ugettext_lazy as _
from djchoices import DjangoChoices, ChoiceItem

# Automatically figure out the ROOT_DIR and PROJECT_DIR.
DJANGO_PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
ROOT_DIR = os.path.abspath(os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir))

#
# Standard Django settings.
#

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

LANGUAGES = (
    ('nl', 'Nederlands'),
)
LANGUAGE_CODE = 'nl'

LOCALE_PATHS = (
    os.path.join(DJANGO_PROJECT_DIR, 'locale'),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

SITE_ID = 1

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
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DJANGO_PROJECT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h7fj5&l=^u5e2lf^v^-p=ze%a57x6byw7uoihxllpl)j^-k+#u'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',

    'langerak_gkv.homepage.context_processors.sidebar',
    'langerak_gkv.users.context_processors.login',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
WSGI_APPLICATION = 'langerak_gkv.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DJANGO_PROJECT_DIR, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(DJANGO_PROJECT_DIR, 'fixtures'),
)

INSTALLED_APPS = [

    'djamin',
    # Note: contenttypes should be first, see Django ticket #10827
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # External applications.
    'axes',
    'django_mailer',
    'south',
    'compressor',
    'easy_thumbnails',
    'leaflet',
    'formulation',
    'rest_framework',
    'rosetta',
    'haystack',
    'aldryn_search',
    'django_extensions',
    # 'sorl.thumbnail',
    'newsletter',
    'import_export',
    'image_cropping',
    'password_reset',

    # cms
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_video',
    'cmsplugin_filer_link',
    'cms',
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
    'langerak_gkv.users',
    'langerak_gkv.utils',
    'langerak_gkv.worklog',
    'langerak_gkv.migration',
]

LOGGING_DIR = os.path.join(ROOT_DIR, 'log')

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
            'class': 'django.utils.log.NullHandler',
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
EMAIL_BACKEND = 'django_mailer.smtp_queue.EmailBackend'

#
# Django-axes
#
AXES_LOGIN_FAILURE_LIMIT = 3  # Default: 3
AXES_LOCK_OUT_AT_FAILURE = True  # Default: True
AXES_USE_USER_AGENT = False  # Default: False

#
# Auth
#

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'langerak_gkv.users.backends.UsernameModelBackend',
)
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = '/'


#
# South
#
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


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
            'size': (120, 90),
            'crop': True,
            'upscale': True,
        },
        'avatar_portrait': {
            'size': (300, 320),
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
EMAIL_POD = 'pod@koningskerk.nu'
EMAIL_ORGANIST = 'organist@koningskerk.nu'
EMAIL_BEAMIST = 'beamist@koningskerk.nu'


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
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter',]

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
                    u'tokenizer': u'standard'  # Required for searching numbers: http://stackoverflow.com/questions/13636419/elasticsearch-edgengrams-and-numbers
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
