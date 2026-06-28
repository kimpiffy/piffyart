from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "shop/product_list.html", {"page_title": "Shop", "page_tag": "shop", "page_body": "Products will be managed through the database and shown here.", "products": products})