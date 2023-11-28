# Generated by Django 4.2.7 on 2023-11-28 17:30

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_delete_storeinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(validators=[products.models.non_negative_validator])),
                ('country_of_origin', models.CharField(max_length=220)),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='products_inventory', to='products.products')),
                ('store_name', models.ManyToManyField(blank=True, related_name='store_inventory', to='products.store')),
            ],
        ),
    ]