from django.shortcuts import render

from shop.froms import AddressForm

from shop.models import Client, Address

from shop.views.cart_view import prepare_products_from_cart

from shop.views.order_view import get_client_personal_data_from_db


def add_address(request):
    if request.method == "POST":
        form = AddressForm(data=request.POST)
        if form.is_valid():
            client = Client.objects.filter(pk=request.user.pk).first()
            address = form.save(commit=False)
            address.client = client
            address.save()
            cart = request.session.get("cart")
            addresses = Address.objects.filter(client=client).all()
            products, cart_value = prepare_products_from_cart(cart)
            personal_data = get_client_personal_data_from_db(client)

            return render(
                request,
                "shop/order/confirm_order_logged_user.html",
                {
                    "addresses": addresses,
                    "personal_data": personal_data,
                    "cart": cart,
                    "products": products,
                    "cart_value": cart_value,
                },
            )
    else:
        form = AddressForm()
    return render(request, "shop/order/order.html", {"form": form})

