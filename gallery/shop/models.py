from django.db import models
from art.models import Product
from account.models import User


class Order(models.Model):
    order_date = models.DateField(blank=True, null=True)
    acceptance_date = models.DateField(blank=True, null=True)
    realization_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return "{}, {}".format(self.order_date, self.acceptance_date)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.user.first_name, self.user.last_name)


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, ul.  {}, {}, kod pocztowy {}".format(
            self.city, self.street, self.number, self.zip_code
        )


class OrderProduct(models.Model):
    product = models.ManyToManyField(Product)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE, blank=True, null=True)
