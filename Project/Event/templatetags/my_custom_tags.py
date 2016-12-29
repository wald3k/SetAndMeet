from django import template

register = template.Library()
#http://stackoverflow.com/questions/8948430/get-list-item-dynamically-in-django-templates
#This tag enables to get item from a python list[]
@register.filter
def lookup(d, key):
    return d[key]

    #Use it like that:
    # {{ mylist|lookup:x }}