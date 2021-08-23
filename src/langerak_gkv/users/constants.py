from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class Sex(DjangoChoices):
    male = ChoiceItem("male", _("male"))
    female = ChoiceItem("female", _("female"))
