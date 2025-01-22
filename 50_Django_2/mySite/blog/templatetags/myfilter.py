from django import template

register = template.Library()

@register.filter
def multiply_by(value, arg):
    return value * arg



@register.simple_tag
def plus(value,tag):
    return value+tag