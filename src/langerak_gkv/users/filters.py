from datetime import date

from django import forms
from django.db.models import Q
from django.template.defaultfilters import capfirst
from django.utils.translation import gettext_lazy as _

import django_filters

from .constants import Sex
from .models import District, DistrictFunction, User


class IntegerFilter(django_filters.NumberFilter):
    field_class = forms.IntegerField


class UserSearchFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(
        method="filter_full_name", label=_("Name"), required=False
    )
    query = django_filters.CharFilter(
        method="filter_query", label=_("Search terms"), required=False
    )

    min_age = IntegerFilter(
        method="filter_by_age", label=_("Minimum age"), required=False
    )
    max_age = IntegerFilter(
        method="filter_by_age", label=_("Maximum age"), required=False
    )
    sex = django_filters.MultipleChoiceFilter(
        label=_("Gender"),
        required=False,
        choices=Sex.choices,
        widget=forms.CheckboxSelectMultiple,
    )
    first_name = django_filters.CharFilter(
        field_name="first_name",
        lookup_expr="icontains",
        label=capfirst(_("first name")),
    )
    last_name = django_filters.CharFilter(
        field_name="last_name", lookup_expr="icontains", label=capfirst(_("last name"))
    )
    address = django_filters.CharFilter(
        field_name="address",
        lookup_expr="icontains",
        label=capfirst(_("street")),
        help_text=_("Street name and number or parts of the address."),
    )
    district = django_filters.ModelChoiceFilter(
        field_name="district",
        lookup_expr="exact",
        queryset=District.objects.order_by("name"),
        label=capfirst(_("district")),
    )
    district_function = django_filters.ModelChoiceFilter(
        field_name="district_function",
        lookup_expr="exact",
        queryset=DistrictFunction.objects.order_by("name"),
        label=capfirst(_("district function")),
    )

    class Meta:
        model = User
        fields = ()

    def filter_full_name(self, queryset, name, value):
        bits = value.split()
        q = Q()
        for bit in bits:
            q |= Q(first_name__icontains=bit) | Q(last_name__icontains=bit)

        return queryset.filter(q)

    def filter_query(self, queryset, name, value):
        bits = value.split()
        q = Q()
        for bit in bits:
            q |= (
                Q(first_name__icontains=bit)
                | Q(last_name__icontains=bit)
                | Q(about_me__icontains=bit)
            )
        return queryset.filter(q)

    def filter_by_age(self, queryset, name, value):
        assert name in ["min_age", "max_age"]
        this_year = date.today().year
        birth_year = this_year - value

        if name == "min_age":
            lookup = "birthdate__lte"
            filter_value = date(birth_year, 1, 1)
        elif name == "max_age":
            lookup = "birthdate__gte"
            filter_value = date(birth_year, 12, 31)
        return queryset.filter(**{lookup: filter_value})
