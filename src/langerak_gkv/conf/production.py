from .base import *  # noqa

DEBUG = False

LOGGING["loggers"].update(
    {
        "langerak_gkv": {
            "handlers": ["project"],
            "level": "WARNING",
            "propagate": True,
        },
        "django": {"handlers": ["django"], "level": "WARNING", "propagate": True},
    }
)
