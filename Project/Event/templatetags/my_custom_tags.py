from django import template

register = template.Library()
#http://stackoverflow.com/questions/8948430/get-list-item-dynamically-in-django-templates
#http://stackoverflow.com/questions/5493776/django-current-tags-is-not-a-valid-tag-library
#This tag enables to get item from a python list[]
@register.filter
def lookup(d, key):
    return d[key]

    #Use it like that:
    # {{ mylist|lookup:x }}