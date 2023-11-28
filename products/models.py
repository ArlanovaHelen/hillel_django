from django.db import models
from django.core.exceptions import ValidationError

def non_negative_validator(value):
    if value<0:
        raise ValidationError('Price cann`t be negative!')


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=220, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
class Store(models.Model):
    name = models.CharField(max_length=40)
    working_days = models.CharField(max_length=40)
    opening_hours = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    delivery = models.BooleanField()
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=220)
    price = models.FloatField(validators=[non_negative_validator])
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT, related_name='products', null=True)
    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return self.name
class StoreInventory(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.RESTRICT, related_name='products_inventory', null=True)
    store_name = models.ManyToManyField(Store, related_name='store_inventory', blank=True)
    quantity = models.FloatField(validators=[non_negative_validator])
    country_of_origin = models.CharField(max_length=220)
