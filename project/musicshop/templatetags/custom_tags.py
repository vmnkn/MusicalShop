from django import template
from datetime import datetime
from django.contrib.auth.models import User
from musicshop.models import Basket


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


@register.simple_tag(name='cart', takes_context=True)
def cart(context):
    request = context['request']
    if request.user.is_authenticated:
        cart = sum(basket.quantity for basket in Basket.objects.filter(user=request.user))
    else:
        cart = 0
    return cart
