from django.template.defaultfilters import stringfilter, register


@register.filter
def to_int(value):
    return value