from django_filters import FilterSet
from .models import Guitar


class GuitarFilter(FilterSet):
    class Meta:
        model = Guitar  # модель
        fields = {  # словарь настройки фильтров
            'name': ['icontains'],  # поиск по названию
            'quantity': ['gt'],  # greater-than - больше чем
            'price': [
                'lt',
                'gt',
            ]
        }
