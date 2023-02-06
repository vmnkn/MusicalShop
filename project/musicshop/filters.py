from django_filters import FilterSet, CharFilter, ModelChoiceFilter, NumberFilter
from .models import Guitar, Category, Manufacturer
from django import forms


class GuitarFilter(FilterSet):
    search_name = CharFilter(
        field_name='name',
        label='Guitar name',
        lookup_expr='icontains',
    )

    search_material = CharFilter(
        field_name='material',
        label='Material',
        lookup_expr='icontains',
    )

    search_category = ModelChoiceFilter(
        empty_label='All categories',
        field_name='category',
        label='Category',
        queryset=Category.objects.all(),
    )

    search_manufacturer = ModelChoiceFilter(
        empty_label='All manufacturers',
        field_name='manufacturer',
        label='Manufacturer',
        queryset=Manufacturer.objects.all(),
    )

    search_strings = NumberFilter(
        field_name='strings_number',
        label='Strings',
    )

    search_lads = NumberFilter(
        field_name='lads_number',
        label='Lads',
    )

    search_price = NumberFilter(
        field_name='price',
        label='Price',
        lookup_expr='gt',
    )
