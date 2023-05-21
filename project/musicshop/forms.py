from django import forms
from .models import Guitar


class GuitarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Category not selected'
        self.fields['manufacturer'].empty_label = 'Manufacturer not selected'

    class Meta:
        model = Guitar
        fields = ['name', 'description', 'photo', 'quantity', 'price', 'sale', 'sale_price', 'material', 'color',
                  'strings_number', 'lads_number', 'manufacturer', 'category', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

