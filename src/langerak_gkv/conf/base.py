import os

from django.urls import reverse_lazy

from .cms import *  # noqa

# Automatically figure out the BASE_DIR and PROJECT_DIR.
DJANGO_PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir)
)
BASE_DIR = os.path.abspath(
    os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir)
)

#
# Standard Django settings.
#

DEBUG = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv("SECRET_KEY")

ADMINS = (("Sergei Maertens", "sergeimaertens@gmail.com"),)
MANAGERS = ADMINS

LANGUAGES = (("nl", "Nederlands"),)
LANGUAGE_CODE = "nl"

LOCALE_PATHS = (os.path.join(DJANGO_PROJECT_DIR, "locale"),)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    "dummy": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "Europe/Amsterdam"

SITE_ID = int(os.getenv("SITE_ID", "1"))

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
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

FILE_UPLOAD_PERMISSIONS = 0o644

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DJANGO_PROJECT_DIR, "static"),
    # 3rd party NPM deps
    ("normalize.css", os.path.join(BASE_DIR, "node_modules", "normalize.css")),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(DJANGO_PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "cms.context_processors.cms_settings",
                "sekizai.context_processors.sekizai",
                "langerak_gkv.homepage.context_processors.sidebar",
                "langerak_gkv.homepage.context_processors.home",
                "langerak_gkv.users.context_processors.login",
            ]
        },
    }
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "axes.middleware.AxesMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # External middleware.
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
    "cms.middleware.utils.ApphookReloadMiddleware",
]

ROOT_URLCONF = "langerak_gkv.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "wsgi.application"


FIXTURE_DIRS = (os.path.join(DJANGO_PROJECT_DIR, "fixtures"),)

INSTALLED_APPS = [
    # Note: contenttypes should be first, see Django ticket #10827
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    # order matters, needed for cms migrations
    "langerak_gkv.users",
    # External applications.
    "axes",
    "django_yubin",
    "easy_thumbnails",
    "leaflet",
    "sniplates",
    "rest_framework",
    "rosetta",
    "haystack",
    "import_export",
    "image_cropping",
    "password_reset",
    "django_bleach",
    # cms
    "cms",
    "treebeard",
    "djangocms_text_ckeditor",
    "filer",
    "djangocms_file",
    "djangocms_picture",
    "djangocms_video",
    "djangocms_link",
    "menus",
    "sekizai",
    # Project applications.
    "langerak_gkv.activities",
    "langerak_gkv.homepage",
    "langerak_gkv.liturgies",
    "langerak_gkv.mailing",
    "langerak_gkv.search",
    "langerak_gkv.societies",
    "langerak_gkv.utils",
]

LOGGING_DIR = os.path.join(BASE_DIR, "log")

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(name)s %(module)s %(process)d %(thread)d  %(message)s"
        },
        "timestamped": {"format": "%(asctime)s %(levelname)s %(name)s  %(message)s"},
        "simple": {"format": "%(levelname)s  %(message)s"},
        "performance": {"format": "%(asctime)s %(process)d | %(thread)d | %(message)s"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "timestamped",
        },
        "django": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGGING_DIR, "django.log"),
            "formatter": "verbose",
        },
        "project": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGGING_DIR, "langerak_gkv.log"),
            "formatter": "verbose",
        },
        "performance": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGGING_DIR, "performance.log"),
            "formatter": "performance",
        },
    },
    "loggers": {
        "langerak_gkv": {"handlers": ["project"], "level": "INFO", "propagate": True},
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
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
EMAIL_BACKEND = "django_yubin.smtp_queue.EmailBackend"

#
# Django-axes
#
AXES_ENABLED = False
AXES_CACHE = "dummy"
AXES_LOGIN_FAILURE_LIMIT = 3  # Default: 3
AXES_LOCK_OUT_AT_FAILURE = True  # Default: True
AXES_USE_USER_AGENT = False  # Default: False

IPWARE_META_PRECEDENCE_ORDER = (
    "HTTP_X_REAL_IP",
    "HTTP_X_FORWARDED_FOR",
    "X_FORWARDED_FOR",  # <client>, <proxy1>, <proxy2>
    "HTTP_CLIENT_IP",
    "HTTP_X_FORWARDED",
    "HTTP_X_CLUSTER_CLIENT_IP",
    "HTTP_FORWARDED_FOR",
    "HTTP_FORWARDED",
    "HTTP_VIA",
    "REMOTE_ADDR",
)

#
# Auth
#

AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
    "langerak_gkv.users.backends.EmailModelBackend",
]
LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = reverse_lazy("pages-root")

#
# GEO
#
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (51.93, 4.876),
    "DEFAULT_ZOOM": 9,
    # 'TILES': [(_('Streets'), 'http://openmapsurfer.uni-hd.de/tiles/roads/x={x}&y={y}&z={z}', {
    #     'minZoom': 0, 'maxZoom': 20, 'attribution': '',
    # })]
}

#
# EMAIL addresses
#
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_POD = "pod@langerak.gkv.nl"
EMAIL_ORGANIST = "organist@langerak.gkv.nl"
EMAIL_BEAMIST = "beamist@langerak.gkv.nl"
EMAIL_KOSTER = "koster@langerak.gkv.nl"
EMAIL_PREACHER = "predikant@langerak.gkv.nl"
EMAIL_BIBLE_GROUP = "bijbelleesgroep@langerak.gkv.nl"
EMAIL_PREACH_CREATION = "preekvoorziening@langerak.gkv.nl"


#
# Django-haystack
#
HAYSTACK_CONNECTIONS = {
    "default": {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        "ENGINE": "langerak_gkv.search.backends.ConfigurableElasticSearchEngine",
        "URL": os.getenv("ELASTIC_SEARCH", "http://127.0.0.1:9200/"),
        "INDEX_NAME": os.getenv("ELASTIC_INDEX", "gklangerak"),
    }
}

ELASTICSEARCH_INDEX_SETTINGS = {
    "settings": {
        "analysis": {
            "filter": {
                "haystack_edgengram": {
                    "max_gram": 30,  # Default: 15. Make this larger to ensure long words are properly found
                    "type": "edgeNGram",
                    "min_gram": 2,  # Default: 2. Keep this small to ensure we get results for partial words
                },
                "haystack_ngram": {
                    "max_gram": 15,
                    "type": "nGram",
                    "min_gram": 2,  # Default: 3
                },
            },
            "tokenizer": {
                "haystack_edgengram_tokenizer": {
                    "max_gram": 15,
                    "type": "edgeNGram",
                    # u'side': u'front',
                    "min_gram": 2,
                },
                "haystack_ngram_tokenizer": {
                    "max_gram": 15,
                    "type": "nGram",
                    "min_gram": 2,
                },
            },
            "analyzer": {
                "edgengram_analyzer": {
                    "filter": ["lowercase", "haystack_edgengram"],
                    "type": "custom",
                    # Required for searching numbers:
                    # http://stackoverflow.com/questions/13636419/elasticsearch-edgengrams-and-numbers
                    "tokenizer": "standard",
                },
                "ngram_analyzer": {
                    "filter": ["haystack_ngram"],
                    "type": "custom",
                    "tokenizer": "lowercase",
                },
            },
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
# BLEACH HTML sanitizer
#
BLEACH_ALLOWED_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'br',
    'blockquote',
    'code',
    'em',
    'i',
    'li',
    'ol',
    'strong',
    'ul',
]

#
# Tests
#
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Raven
SENTRY_DSN = os.getenv("SENTRY_DSN")

if SENTRY_DSN:
    import raven

    INSTALLED_APPS = INSTALLED_APPS + ["raven.contrib.django.raven_compat"]

    RAVEN_CONFIG = {"dsn": SENTRY_DSN, "release": raven.fetch_git_sha(BASE_DIR)}
    LOGGING["handlers"].update(
        {
            "sentry": {
                "level": "WARNING",
                "class": "raven.handlers.logging.SentryHandler",
                "dsn": RAVEN_CONFIG["dsn"],
            }
        }
    )
