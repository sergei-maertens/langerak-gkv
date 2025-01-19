from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

#
# Easy thumbnails
#
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_ALIASES = {
    "": {
        "default": {"size": (400, 300), "crop": True, "upscale": True},
        "homepage": {"size": (300, 300), "crop": True, "upscale": True},
        "small": {"size": (120, 120), "crop": True, "upscale": True},
        "avatar_portrait": {"size": (300, 300), "crop": True, "upscale": True},
        "header": {"size": (1170, 315), "crop": True, "upscale": True},
        "birthday": {"size": (50, 50), "crop": True, "upscale": True},
        "activity_detail": {"size": (800, 400), "crop": True, "upscale": True},
    }
}

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

#
# Django CMS
#
CMS_PERMISSION = True

CMS_TEMPLATES = (
    ("cms/default.html", _("Default")),
    ("homepage/home.html", _("Homepage")),
    ("cms/3_columns.html", _("3 Columns (responsive)")),
)

_homepage_slot_conf = {"plugins": ["HomepageLinkPlugin"]}

CMS_PLACEHOLDER_CONF = {
    "header image": {"plugins": ["PicturePlugin"], "limits": {"global": 1}},
    "slot11": _homepage_slot_conf,
    "slot12": _homepage_slot_conf,
    "slot13": _homepage_slot_conf,
    "slot21": _homepage_slot_conf,
    "slot22": _homepage_slot_conf,
    "slot23": _homepage_slot_conf,
    "slot31": _homepage_slot_conf,
    "slot32": _homepage_slot_conf,
    "slot33": _homepage_slot_conf,
}

DJANGOCMS_PICTURE_ALIGN = (("header", _("header top image")),)


class FilerStyles(TextChoices):
    default = " ", _("Default")
    orange = "orange", _("Orange")
    blue = "blue", _("Blue")
    green = "green", _("Green")
    purple = "purple", _("Purple")
    orange_rm = "orange read-more", _("Read-more orange")
    blue_rm = "blue read-more", _("Read-more blue")
    green_rm = "green read-more", _("Read-more green")
    purple_rm = "purple read-more", _("Read-more purple")


FILER_LINK_STYLES = FilerStyles.choices
