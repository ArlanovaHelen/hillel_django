# Generated by Django 4.2.7 on 2023-11-28 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_storeinventory_product_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoreInventory',
        ),
    ]
