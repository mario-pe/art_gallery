from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Cart

from art.models import Product

from shop.models import Client

from shop.froms import OrderProductForm


def cart(request):
    if request.session.get("cart"):
        cart = request.session.get("cart")
        products = []
        import ipdb
        ipdb.set_trace()
        for c in cart:
            product = Product.objects.filter(pk=c.get("product_id")).first()
            products.append(product)

    return render(request, "shop/cart/cart.html", {"products": products})


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
        return redirect("art:product_details", product_id=product_id)
    else:
        form = OrderProductForm(initial={"quantity": 1})
        return render(
            request, "shop/cart/add_to_cart.html", {"form": form, "product": product}
        )


def confirm_add_to_cart(request):

    oder_product = "order prod"
    return render(request, "shop/cart/add_to_cart.html", {"oder_product": oder_product})
