from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Guitar(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    strings_number = models.IntegerField(validators=[MinValueValidator(0)])
    lads_number = models.IntegerField(validators=[MinValueValidator(0)])

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('guitar_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name

