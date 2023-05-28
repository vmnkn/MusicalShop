from .models import *
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class TCategory(TranslationOptions):
    class Meta:
        model = Category
        fields = '__all__'


@register(User)
class TUser(TranslationOptions):
    class Meta:
        model = User
        fields = '__all__'


@register(Product)
class TProduct(TranslationOptions):
    class Meta:
        model = Product
        fields = '__all__'


@register(Basket)
class TBasket(TranslationOptions):
    class Meta:
        model = Basket
        fields = '__all__'


@register(Material)
class TMaterial(TranslationOptions):
    class Meta:
        model = Material
        fields = '__all__'


@register(Manufacturer)
class TManufacturer(TranslationOptions):
    class Meta:
        model = Manufacturer
        fields = '__all__'


