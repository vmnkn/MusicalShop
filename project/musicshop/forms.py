from django import forms
from .models import Guitar


class GuitarForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))

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

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

