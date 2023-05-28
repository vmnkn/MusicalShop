from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class TABasket(TranslationAdmin):
    model = Basket


class TACategory(TranslationAdmin):
    model = Category


class TAMaterial(TranslationAdmin):
    model = Material


class TAManufacturer(TranslationAdmin):
    model = Manufacturer


class TAProduct(TranslationAdmin):
    model = Product


admin.site.register(Basket)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Manufacturer)
admin.site.register(Product)
