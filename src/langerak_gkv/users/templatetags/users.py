from datetime import date, timedelta

from django import template

from ..models import User

register = template.Library()


@register.inclusion_tag('users/birthdays.html')
def show_birthdays(weeks=3):
    today = date.today()
    upper_limit = today + timedelta(weeks=weeks)

    month, year = today.month, today.year
    qs = User.objects.none()
    while (month, year) <= (upper_limit.month, upper_limit.year):
        qs |= User.objects.only_real().filter(birthdate__month=month)
        month = (month+1)
        if month == 13:
            month = 1
            year += 1

    users = [
        user for user in qs.distinct()
        if today <= user.birthdate.replace(year=today.year) <= upper_limit
    ]

    return {
        'weeks': weeks,
        'birthday_users': sorted(users, key=lambda u: (u.birthdate.replace(year=today.year)))
    }
