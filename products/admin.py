from django.contrib import admin
from products.models import Products, Category, Tag, Store, StoreInventory
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Store)
admin.site.register(StoreInventory)
# Register your models here.
