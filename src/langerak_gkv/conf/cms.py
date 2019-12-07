from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices

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
    "image_cropping.thumbnail_processors.crop_corners",
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
    ("cms/right_sidebar.html", _("Content left, sidebar right")),
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


class FilerStyles(DjangoChoices):
    default = ChoiceItem(" ", _("Default"))
    orange = ChoiceItem("orange", _("Orange"))
    blue = ChoiceItem("blue", _("Blue"))
    green = ChoiceItem("green", _("Green"))
    purple = ChoiceItem("purple", _("Purple"))
    orange_rm = ChoiceItem("orange read-more", _("Read-more orange"))
    blue_rm = ChoiceItem("blue read-more", _("Read-more blue"))
    green_rm = ChoiceItem("green read-more", _("Read-more green"))
    purple_rm = ChoiceItem("purple read-more", _("Read-more purple"))


FILER_LINK_STYLES = FilerStyles.choices
