from django import template

register = template.Library()


@register.filter
def phone(phone_nr):
    try:
        numbers = [char for char in phone_nr if char.isdigit()]
        return "{0}-{1}".format(''.join(numbers[:4]), ''.join(numbers[4:]))
    except:
        return phone_nr
