from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class Sex(DjangoChoices):
    male = ChoiceItem("male", _("male"))
    female = ChoiceItem("female", _("female"))


class MemberType(DjangoChoices):
    baptised = ChoiceItem("baptised", _("baptised member"))
    practicing = ChoiceItem("practicing", _("practicing member"))
    guest = ChoiceItem("guest", _("guest member"))
