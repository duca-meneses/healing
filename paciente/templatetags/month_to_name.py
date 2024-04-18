import calendar
import locale
from django import template

register = template.Library()

@register.filter
def month_to_name(month_number):
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    return calendar.month_name[int(month_number)]

@register.filter
def day_to_name(day_number):
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    return calendar.day_name[int(day_number)]