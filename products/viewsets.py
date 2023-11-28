from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from products.serializers import ProductSerializer, ProductViewSerializer, CategoryWithProductsSerializer, StoreSerializer, StoreWithProductsSerializer
from products.models import Products, Category, Store
from products.permissions import MyCustomPermission
#from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all().select_related('category').prefetch_related('tags')
    permission_classes = (MyCustomPermission,)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductViewSerializer
        else:
            return ProductSerializer
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().prefetch_related('products')
    serializer_class=CategoryWithProductsSerializer

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all().prefetch_related('products')
    serializer_class=StoreWithProductsSerializer