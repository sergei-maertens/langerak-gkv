from django.shortcuts import redirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _


def send_liturgy_email(modeladmin, request, queryset):
    pks = list(queryset.values_list("pk", flat=True))
    liturgies = list(
        queryset.order_by("liturgy__id").values_list("liturgy_id", flat=True).distinct()
    )
    mvd = MultiValueDict({"pk": pks, "liturgy": liturgies})
    url = "{}?{}".format(reverse("admin:send_liturgy_email"), urlencode(mvd, True))
    return redirect(url)


send_liturgy_email.short_description = _("Compose and send e-mail")
