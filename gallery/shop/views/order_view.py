from django.shortcuts import render, redirect

from shop.models import Order
from shop.views.cart_view import prepare_products_from_cart

from shop.froms import NoLoggedUserOrder


def make_no_logged_user_order(request):
    if request.method == "POST":
        form = NoLoggedUserOrder(data=request.POST)
        if form.is_valid():
            personal_data = __get_client_personal_data_from_form(form)
            cart = request.session.get("cart")
            products, cart_value = prepare_products_from_cart(cart)
            return render(
                request,
                "shop/order/confirm_order.html",
                {
                    "personal_data": personal_data,
                    "cart": cart,
                    "products": products,
                    "cart_value": cart_value,
                },
            )

    else:
        form = NoLoggedUserOrder()
    return render(request, "shop/order/order.html", {"form": form})


def __get_client_personal_data_from_form(form):
    personal_data = {}
    personal_data["first_name"] = form.data.get("first_name")
    personal_data["second_name"] = form.data.get("second_name")
    personal_data["email"] = form.data.get("email")
    personal_data["street"] = form.data.get("street")
    personal_data["number"] = form.data.get("number")
    personal_data["zip_code"] = form.data.get("zip_code")
    personal_data["city"] = form.data.get("city")
    return personal_data
