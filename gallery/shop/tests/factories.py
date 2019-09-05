from datetime import datetime

import factory

from shop.models import Address, Cart, Client, Order

class AddressFactory(factory.DjangoModelFactory):
    pass

class CartFactory(factory.DjangoModelFactory):
    pass

class ClientFactory(factory.DjangoModelFactory):
    pass

class OrderFactory(factory.DjangoModelFactory):
    pass