from django import forms
from .models import Guitar


class GuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = [
            'name',
            'description',
            'quantity',
            'price',
            'material',
            'color',
            'strings_number',
            'lads_number',
            'manufacturer',
            'category',
        ]
