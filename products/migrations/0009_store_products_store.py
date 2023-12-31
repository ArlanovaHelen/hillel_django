# Generated by Django 4.2.7 on 2023-11-28 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_tag_products_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('working_days', models.CharField(max_length=40)),
                ('opening_hours', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('delivery', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='products.store'),
        ),
    ]
