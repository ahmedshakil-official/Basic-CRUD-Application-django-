from django import template

register = template.Library()


def add_string(value):
    return value+" (Warfaze)"


register.filter('add_st', add_string)