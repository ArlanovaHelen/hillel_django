from rest_framework import serializers
from products.models import Products, Category, Tag, Store

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'working_days', 'opening_hours', 'location', 'delivery')
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'category', 'tags', 'store')

class ProductViewSerializer(ProductSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    store = StoreSerializer()

class CategoryWithProductsSerializer(CategorySerializer):
    products = ProductSerializer(many=True)
    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ('products',)

class StoreWithProductsSerializer(StoreSerializer):
    products = ProductSerializer(many=True)
    class Meta(StoreSerializer.Meta):
        fields = StoreSerializer.Meta.fields + ('products',)