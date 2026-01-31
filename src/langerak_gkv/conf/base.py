import os

from django.urls import reverse_lazy

import sentry_sdk

from .cms import *  # noqa
from .utils import config, get_current_version, get_sentry_integrations

# Automatically figure out the BASE_DIR and PROJECT_DIR.
DJANGO_PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir)
)
BASE_DIR = os.path.abspath(
    os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir)
)

IS_HTTPS = config("IS_HTTPS", default=True)

#
# Standard Django settings.
#

DEBUG = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = config("SECRET_KEY")

ADMINS = (("Sergei Maertens", "info@regex-it.nl"),)
MANAGERS = ADMINS

LANGUAGES = (("nl", "Nederlands"),)
LANGUAGE_CODE = "nl"

LOCALE_PATHS = (os.path.join(DJANGO_PROJECT_DIR, "locale"),)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", split=True)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME", "kerkwebsite"),
        "USER": config("DB_USER", "kerkwebsite"),
        "PASSWORD": config("DB_PASSWORD", ""),
        "HOST": config("DB_HOST", "localhost"),
        "PORT": config("DB_PORT", 5432),
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    "dummy": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "Europe/Amsterdam"

SITE_ID = config("SITE_ID", default=1)

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
                "langerak_gkv.core.context_processors.globals",
            ]
        },
    }
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
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
    "django_yubin",
    "easy_thumbnails",
    "sniplates",
    "rest_framework",
    "rosetta",
    "haystack",
    "import_export",
    "django_bleach",
    "solo",
    # cms
    "treebeard",
    "cms",
    "djangocms_text",
    "filer",
    "djangocms_file",
    "djangocms_picture",
    "djangocms_video",
    "djangocms_link",
    "menus",
    "sekizai",
    # Project applications.
    "langerak_gkv.activities",
    "langerak_gkv.core",
    "langerak_gkv.homepage",
    "langerak_gkv.liturgies",
    "langerak_gkv.search",
    "langerak_gkv.utils",
]

#
# LOGGING
#
LOG_STDOUT = config("LOG_STDOUT", "").lower() in ["yes", "true", "1"]

LOGGING_DIR = os.path.join(BASE_DIR, "log")

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
        "langerak_gkv": {
            "handlers": ["project"] if not LOG_STDOUT else ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["django"] if not LOG_STDOUT else ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

#
# Additional Django settings
#

SESSION_COOKIE_SECURE = IS_HTTPS
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = IS_HTTPS
CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = "SAMEORIGIN"

#
# Sending EMAIL
#
EMAIL_BACKEND = "django_yubin.backends.QueuedEmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_PORT = config(
    "EMAIL_PORT", default=25
)  # disabled on Google Cloud, use 487 instead
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False)
EMAIL_TIMEOUT = 10

#
# Auth
#

AUTH_USER_MODEL = "users.User"
LOGIN_URL = "admin:login"
LOGIN_REDIRECT_URL = reverse_lazy("pages-root")

#
# EMAIL addresses
#
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="noreply@example.com")


#
# Django-haystack
#
HAYSTACK_CONNECTIONS = {
    "default": {
        # 'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        "ENGINE": "langerak_gkv.search.backends.ConfigurableElasticSearchEngine",
        "URL": config("ELASTIC_SEARCH", "http://127.0.0.1:9200/"),
        "INDEX_NAME": config("ELASTIC_INDEX", "gklangerak"),
    }
}

if "ES_SECURED" in os.environ:
    HAYSTACK_CONNECTIONS["default"]["KWARGS"] = {
        "use_ssl": True,
        "verify_certs": True,
        "http_auth": (config("ELASTIC_USER"), config("ELASTIC_PASSWORD")),
    }


ELASTICSEARCH_INDEX_SETTINGS = {
    "settings": {
        "analysis": {
            "filter": {
                "haystack_edgengram": {
                    "max_gram": 30,  # Default: 15. Make this larger to ensure long words are properly found
                    "type": "edge_ngram",
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
                    "type": "edge_ngram",
                    # u'side': u'front',
                    "min_gram": 2,
                },
                "haystack_ngram_tokenizer": {
                    "max_gram": 15,
                    "type": "ngram",
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
# BLEACH HTML sanitizer
#
BLEACH_ALLOWED_TAGS = [
    "a",
    "abbr",
    "acronym",
    "b",
    "br",
    "blockquote",
    "code",
    "em",
    "i",
    "li",
    "ol",
    "p",
    "strong",
    "ul",
]

#
# Tests
#
TEST_RUNNER = "django.test.runner.DiscoverRunner"

#
# SENTRY - error monitoring
#
SENTRY_DSN = config("SENTRY_DSN", None)
RELEASE = get_current_version()

if SENTRY_DSN:
    SENTRY_CONFIG = {
        "dsn": SENTRY_DSN,
        "release": RELEASE,
    }

    sentry_sdk.init(
        **SENTRY_CONFIG, integrations=get_sentry_integrations(), send_default_pii=True
    )

#
# CELERY - async task queue
#
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# Add (by default) 5 (soft), 15 (hard) minute timeouts to all Celery tasks.
CELERY_TASK_TIME_LIMIT = config("CELERY_TASK_HARD_TIME_LIMIT", default=15 * 60)  # hard
CELERY_TASK_SOFT_TIME_LIMIT = config(
    "CELERY_TASK_SOFT_TIME_LIMIT", default=5 * 60
)  # soft

# Only ACK when the task has been executed. This prevents tasks from getting lost, with
# the drawback that tasks should be idempotent (if they execute partially, the mutations
# executed will be executed again!)
CELERY_TASK_ACKS_LATE = True

# ensure that no tasks are scheduled to a worker that may be running a very long-running
# operation, leading to idle workers and backed-up workers. The `-O fair` option
# *should* have the same effect...
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
