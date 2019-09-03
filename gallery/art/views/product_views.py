from django.shortcuts import render, get_object_or_404
from art.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, 'art/product/products.html', {'products': products})