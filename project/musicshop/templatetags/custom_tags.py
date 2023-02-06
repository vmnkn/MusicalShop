from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag(name='current_time')
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


@register.simple_tag(name='url_replace', takes_context=True)  # для работы тега необходимо передать контекст
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()  # позволяет скопировать все элементы текущего запроса
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()
