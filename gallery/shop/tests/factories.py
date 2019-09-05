from datetime import datetime

import factory

from shop.models import Address, Cart, Client, Order
from art.tests.factories import ProductFactory

class AddressFactory(factory.DjangoModelFactory):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class CartFactory(factory.DjangoModelFactory):
    quantity = models.IntegerField()
    value = models.DecimalField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

class OrderFactory(factory.DjangoModelFactory):
    order_date = datetime.now()
    acceptance_date =datetime.now()
    realization_date =datetime.now()
    payment_date = datetime.now()
    products = factory.SubFactory(ProductFactory)


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda a: "User_name{}".format(a + 1))
    first_name = factory.Sequence(lambda a: "Second_name_{}".format(a + 1))
    last_name = factory.Sequence(lambda a: "Second_name_{}".format(a + 1))

class ClientFactory(factory.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    products = factory.SubFactory(ProductFactory)

