from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Cart

from art.models import Product

from shop.models import Client

from shop.froms import OrderProductForm


def cart(request):
    if request.session.get("cart"):
        cart = request.session.get("cart")
        products = []
        for c in cart:
            product = Product.objects.filter(pk=c.get("product_id")).first()
            product.quantity = c.get("quantity")
            products.append(product)
        return render(request, "shop/cart/cart.html", {"products": products})
    return render(request, "shop/cart/cart.html")


def add_to_cart(request, product_id):
    product = Product.objects.filter(pk=product_id).first()

    if request.method == "POST":
        form = OrderProductForm(data=request.POST)
        if form.is_valid():
            quantity = form.data.get("quantity")
            if request.session.get("cart"):
                cart = request.session.get("cart")
                order_product = {
                    "product_id": product_id,
                    "quantity": quantity,
                }
                cart.append(order_product)
                request.session["cart"] = cart
            else:
                cart = []
                order_product = {
                    "product_id": product_id,
                    "quantity": quantity,
                }
                cart.append(order_product)
                request.session["cart"] = cart
        return redirect("shop:cart")
    else:
        form = OrderProductForm(initial={"quantity": 1})
        return render(
            request, "shop/cart/add_to_cart.html", {"form": form, "product": product}
        )


def remove_from_cart(request, product_id):
    cart = request.session.get("cart")
    for item in cart:
        if item.get("product_id") == product_id:
            cart.remove(item)
            request.session["cart"] = cart
    return redirect("shop:cart")
