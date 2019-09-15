from django.shortcuts import render

from shop.views.cart_view import prepare_products_from_cart
from art.models import Product

from shop.froms import NoLoggedUserOrder
from django.core.mail import send_mail


def prepare_no_logged_user_order(request):
    if request.method == "POST":
        form = NoLoggedUserOrder(data=request.POST)
        if form.is_valid():
            personal_data = __get_client_personal_data_from_form(form)
            request.session["personal_data"] = personal_data
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


def make_no_logged_user_order(request):
    personal_data = request.session["personal_data"]
    cart = request.session.get("cart")
    products, cart_value = prepare_products_from_cart(cart)

    message = __prepare_email_message(personal_data, products, cart_value)
    send_mail(
        "Potwirdzenie zamowienia w Galerii Parczyńskich",
        message,
        "mariusz-perkowski@wp.pl",
        # ["perkowski.mar@gmail.com"],
        [personal_data.get("email"), "jolanta_parczynska@wp.pl"],
        fail_silently=False,
    )
    products = Product.objects.all()
    return render(request, "art/product/products.html", {"products": products})


def __prepare_email_message(personal_data, products, cart_value):
    message = ""
    header = (
        "Potwierdzajacy złożenia zamówienia W Galerii Parczyńskich \n"
        " Wartość zamowienia: {}. \n "
        "Pieniadze nalezy przelac na konto nr 1234. \n".format(cart_value)
    )
    personal_data = __prepare_string_with_personal_data(personal_data)
    product_list = __preapre_sting_with_produckt_list(products)
    message + header + personal_data + product_list
    return message + header + personal_data + product_list


def __prepare_string_with_personal_data(personal_data):
    message = "\n Dane zamawiającego: \n"
    message = message + "imie: {} \n".format(personal_data.get("first_name"))
    message = message + "nazwisko: {}\n".format(personal_data.get("second_name"))
    message = message + "email: {}\n".format(personal_data.get("email"))
    message = message + "ulica: {}\n".format(personal_data.get("street"))
    message = message + "numer domu: {}\n".format(personal_data.get("number"))
    message = message + "kod pocztowy: {}\n".format(personal_data.get("zip_code"))
    message = message + "miasto: {}\n".format(personal_data.get("city"))
    return message


def __preapre_sting_with_produckt_list(products):
    message = "\n Zamówione produkty: \n"
    message = message + "tytuł,  cena, ilość, wartość pozycji \n"
    for product in products:
        prod_string = "{},  {},  {},  {} \n".format(
            product.title, product.price, product.quantity, product.value
        )
        message = message + prod_string
    return message


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
