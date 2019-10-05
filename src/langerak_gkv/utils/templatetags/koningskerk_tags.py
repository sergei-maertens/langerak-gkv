from django import template

register = template.Library()


@register.filter
def pop(value, index=0):
    if isinstance(value, list) and len(value) > 0:
        return value.pop(index)
    return None


@register.simple_tag(takes_context=True)
def absolute_url(context, location=None):
    return context["request"].build_absolute_uri(location)


# @register.inclusion_tag('users/birthdays.html')
# def show_birthdays(weeks=3):
#     today = date.today()
#     upper_limit = today + timedelta(weeks=weeks)

#     month = today.month
#     qs = User.objects.none()
#     while month <= upper_limit.month:
#         qs |= User.objects.filter(birthdate__month=month)
#         month = (month+1)
#         if month == 13:
#             month = 1

#     users = [
#         user for user in qs.distinct()
#         if today <= user.birthdate.replace(year=today.year) <= upper_limit
#     ]

#     return {
#         'weeks': weeks,
#         'birthday_users': sorted(users, key=lambda u: (u.birthdate.replace(year=today.year)))
#     }
