from django import template


register = template.Library()
CURRENCIES_SYMBOLS = {
    'rub': 'P',
    'usd': '$',
}


@register.filter(name='currency')
def currency(value, code='rub'):
    postfix = CURRENCIES_SYMBOLS[code]
    if postfix == '$':
        return f'{round(value / 70)} {postfix}'
    else:
        return f'{value} {postfix}'
