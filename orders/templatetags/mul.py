from django import template

register=template.Library()

@register.simple_tag(name='mul')
def mul(a,b):
    return a*b