from django.shortcuts import render, get_object_or_404

from shop.models import Cart

from art.models import Product

from shop.models import Client


def cart(request, product_id):
    user = Client.objects.all()  #to co z klentem

    cart = Cart.objects.filter(pk=1)  # albo z sessji
    products = Product.objects.filtre(pk=product_id).first()
    # z requesta skąd przyszedl i przekierowac go tam

    return render(request, "art/cart/authors.html", {"products": products})

def add_to_cart(request, product_id):
    pass
