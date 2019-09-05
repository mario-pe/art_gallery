from django.shortcuts import render, get_object_or_404
from art.models import Category, Product


def categories(request):
    categories = Category.objects.all()
    return render(request, "art/category/categories.html", {"categories": categories})


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category_products = Product.objects.filter(category=category_id).all()
    return render(
        request,
        "art/category/category_product.html",
        {"category": category, "category_products": category_products},
    )
