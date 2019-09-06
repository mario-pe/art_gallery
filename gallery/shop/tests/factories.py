from datetime import datetime

import factory

from shop.models import Address, Cart, Client, Order, OrderProduct
from art.tests.factories import ProductFactory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda a: "User_name{}".format(a + 1))
    first_name = factory.Sequence(lambda a: "First_name_{}".format(a + 1))
    last_name = factory.Sequence(lambda a: "Second_name_{}".format(a + 1))


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Order

    order_date = datetime.now()
    acceptance_date = datetime.now()
    payment_date = datetime.now()
    realization_date = datetime.now()
    products = factory.SubFactory(ProductFactory)


class ClientFactory(factory.DjangoModelFactory):
    class Meta:
        model = Client

    order = factory.SubFactory(OrderFactory)
    user = factory.SubFactory(UserFactory)


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address

    city = factory.Sequence(lambda a: "City_{}".format(a + 1))
    street = factory.Sequence(lambda a: "Street_{}".format(a + 1))
    number = factory.Sequence(lambda a: "Number_{}".format(a + 1))
    zip_code = factory.Sequence(lambda a: "20-20{}".format(a + 1))
    client = factory.SubFactory(ClientFactory)


class OrderProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = OrderProduct

    products = factory.SubFactory(ProductFactory)
    order = factory.SubFactory(OrderFactory)
    quantity = factory.Sequence(lambda a: a + 1)
    product_value = factory.Sequence(lambda a: a + 1)


class CartFactory(factory.DjangoModelFactory):
    class Meta:
        model = Cart

    quantity = factory.Sequence(lambda a: a + 1)
    value = factory.Sequence(lambda a: a + 1)
    client = factory.SubFactory(ClientFactory)
    order_product = factory.SubFactory(OrderProduct)
