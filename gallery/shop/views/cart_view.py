from django.shortcuts import render, redirect

from art.models import Product

from shop.froms import OrderProductForm


def cart(request):
    if request.session.get("cart"):
        cart = request.session.get("cart")
        products, cart_value = prepare_products_from_cart(cart)
        return render(
            request,
            "shop/cart/cart.html",
            {"products": products, "cart_value": cart_value},
        )
    return render(request, "shop/cart/cart.html")


def add_to_cart(request, product_id):
    product = Product.objects.filter(pk=product_id).first()

    if request.method == "POST":
        form = OrderProductForm(data=request.POST)
        if form.is_valid():
            quantity = form.data.get("quantity")
            if request.session.get("cart"):
                cart = request.session.get("cart")
                cart = __add_to_cart(product_id, cart, quantity)
                request.session["cart"] = cart
            else:
                cart = []
                order_product = {"product_id": product_id, "quantity": quantity}
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


def __add_to_cart(product_id, products, quantity):
    for product in products:
        if product_id == product.get("product_id"):
            return __add_quantity_if_the_same_product_exist(product, products, quantity)
    return __add_product_to_list(product_id, products, quantity)


def __add_quantity_if_the_same_product_exist(product, products, quantity):
    existing_quantity = product.get("quantity")
    product["quantity"] = int(existing_quantity) + int(quantity)
    return products


def __add_product_to_list(product_id, products, quantity):
    order_product = {"product_id": product_id, "quantity": quantity}
    products.append(order_product)
    return products


def __count_order_product_value(product, quantity):
    value = float(product.price) * int(quantity)
    return round(value, 2)


def __add_product_value_cart_value(cart_value, product):
    cart_value = cart_value + product.value
    return round(cart_value, 2)

def prepare_products_from_cart(cart):
    products = []
    cart_value = 0.00
    for cart_item in cart:
        product = Product.objects.filter(pk=cart_item.get("product_id")).first()
        quantity = cart_item.get("quantity")
        product.quantity = quantity
        product.value = __count_order_product_value(product, quantity)
        cart_value = __add_product_value_cart_value(cart_value, product)
        products.append(product)
    return products, cart_value