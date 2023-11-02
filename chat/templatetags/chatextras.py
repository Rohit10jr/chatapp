from django import template

register = template.Library()

@register.filter(name='initals')
def initials(value):
    initials = ''

    for name in value.split(' '):
        if name and len(initials) < 3:
            initials += name[0].upper()

    return initials 