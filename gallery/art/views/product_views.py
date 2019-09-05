from django.shortcuts import render, get_object_or_404
from art.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, "art/product/products.html", {"products": products})


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "art/product/product_details.html", {"product": product})
