from django_filters import FilterSet, CharFilter, ModelChoiceFilter, NumberFilter
from .models import Product, Category, Manufacturer, Material
from django import forms


class ProductFilter(FilterSet):
    search_name = CharFilter(
        field_name='name',
        label='Название',
        lookup_expr='icontains',
    )

    search_material = ModelChoiceFilter(
        empty_label='Все материалы',
        field_name='material',
        label='Материал',
        queryset=Material.objects.all(),
    )

    search_category = ModelChoiceFilter(
        empty_label='Все категории',
        field_name='category',
        label='Категория',
        queryset=Category.objects.all(),
    )

    search_manufacturer = ModelChoiceFilter(
        empty_label='Все производители',
        field_name='manufacturer',
        label='Производитель',
        queryset=Manufacturer.objects.all(),
    )

    search_price = NumberFilter(
        field_name='price',
        label='Цена',
        lookup_expr='gt',
    )
