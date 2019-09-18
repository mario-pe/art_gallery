import datetime

from django.shortcuts import render

from shop.views.cart_view import prepare_products_from_cart
from art.models import Product

from shop.froms import NoLoggedUserOrder
from django.core.mail import send_mail

from shop.models import Client, Address, Order, OrderProduct


def confirm_order(request):
    if request.user.is_authenticated:
        return prepare_logged_user_order(request)
    else:
        return prepare_no_logged_user_order(request)


def prepare_logged_user_order(request):
    client = Client.objects.filter(pk=request.user.pk).first()
    addresses = Address.objects.filter(client=client).all()
    cart = request.session.get("cart")
    products, cart_value = prepare_products_from_cart(cart)
    personal_data = get_client_personal_data_from_db(client)
    return render(
        request,
        "shop/order/confirm_order_logged_user.html",
        {
            "client": client,
            "addresses": addresses,
            "personal_data": personal_data,
            "cart": cart,
            "products": products,
            "cart_value": cart_value,
        },
    )


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
    send_confirm_mail(message, personal_data["email"])
    products_in_store = Product.objects.all()
    return render(request, "art/product/products.html", {"products": products_in_store})


def make_logged_user_order(request):
    client = Client.objects.filter(pk=request.user.pk).first()
    address_id = request.POST.get("address_id")
    address = Address.objects.filter(pk=address_id).first()
    cart = request.session.get("cart")

    __save_order_to_db(cart, client, address)

    personal_data = get_client_personal_data_from_db(client, address)
    products, cart_value = prepare_products_from_cart(cart)
    message = __prepare_email_message(personal_data, products, cart_value)
    send_confirm_mail(message, personal_data["email"])

    products_in_store = Product.objects.all()
    return render(request, "art/product/products.html", {"products": products_in_store})


def user_order_history(request):
    orders = Order.objects.filter(client_id=request.user.pk).all()
    return render(
        request,
        "shop/order/order_history.html",
        {
            "orders": orders,
        },
    )


def order_details(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    order_produckts = order.order_product.all()
    request.user.pk
    return render(
        request,
        "shop/order/order_details.html",
        {
            "order": order,
            "order_produckts": order_produckts
        },
    )



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
    message = message + "nazwisko: {}\n".format(personal_data.get("last_name"))
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
    personal_data["last_name"] = form.data.get("last_name")
    personal_data["email"] = form.data.get("email")
    personal_data["street"] = form.data.get("street")
    personal_data["number"] = form.data.get("number")
    personal_data["zip_code"] = form.data.get("zip_code")
    personal_data["city"] = form.data.get("city")
    return personal_data


def get_client_personal_data_from_db(client, address=None):
    personal_data = {}
    personal_data["first_name"] = client.user.first_name
    personal_data["last_name"] = client.user.last_name
    personal_data["email"] = client.user.email

    if address:
        personal_data["street"] = address.street
        personal_data["number"] = address.number
        personal_data["city"] = address.city
        personal_data["zip_code"] = address.zip_code


    return personal_data


def __save_order_to_db(cart, client, address):

    order = Order()
    order = add_order_products_to_order(order, cart)
    order.client = client
    order.address = address
    order.order_date = datetime.datetime.now()
    order.save()

def add_order_products_to_order(order, cart):
    order.save()
    for item in cart:
        product = Product.objects.filter(pk=item.get("product_id")).first()
        quantity = item.get("quantity")
        order_product = OrderProduct()
        order_product.quantity = quantity
        order_product.product = product
        import ipdb
        ipdb.set_trace()
        order_product.value = float(product.price) * int(quantity)
        order_product.save()
        order.order_product.add(order_product)
    return order

def send_confirm_mail(message, mail):
    send_mail(
        "Potwirdzenie zamowienia w Galerii Parczyńskich",
        message,
        "mariusz-perkowski@wp.pl",
        # ["perkowski.mar@gmail.com"],
        [mail, "perkowski.mar@gmail.com"],
        fail_silently=False,
    )