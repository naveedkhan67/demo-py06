from django import template

register = template.Library()


def dummy_filter(value, arg):
    return value + " Hello you've been tricked" + arg

register.filter("dummy", dummy_filter)

def format_date(date):
    """Implement something related to date formatting"""
    pass