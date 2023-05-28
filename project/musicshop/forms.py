from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['manufacturer'].empty_label = 'Производитель не выбран'
        self.fields['material'].empty_label = 'Материал не выбран'
        self.fields['name'].label = 'Имя'
        self.fields['description'].label = 'Описание'
        self.fields['photo'].label = 'Изображение'
        self.fields['quantity'].label = 'Количество'
        self.fields['price'].label = 'Цена'
        self.fields['sale'].label = 'Скидка'
        self.fields['sale_price'].label = 'Скидочная цена'
        self.fields['color'].label = 'Цвет'
        self.fields['manufacturer'].label = 'Производитель'
        self.fields['category'].label = 'Категория'
        self.fields['material'].label = 'Материал'

    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'quantity', 'price', 'sale', 'sale_price', 'color', 'manufacturer',
                  'category', 'material']
