from django.http import HttpResponse, JsonResponse, FileResponse
from products.models import Products
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
def hello_world(request):
    return HttpResponse("Hello world!")
def product_count(request):
    count = Products.objects.count()
    return HttpResponse(f'Product Count: {count}')

def products_json_views(request):
    products = Products.objects.all()
    products_json = [{'name': product.name, 'price': product.price, 'description': product.description} for product in products]
    return JsonResponse({'data': products_json})
def cat_view(request):
    file_path = BASE_DIR/'products'/'static'/'kitten.jpg'
    return FileResponse(open(file_path, 'rb'))