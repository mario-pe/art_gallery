from art.models import Product
from art.tests.factories import ProductFactory
from django.test import TestCase


class ProductTests(TestCase):
    def setUp(self) -> None:
        ProductFactory.build().save()
        ProductFactory.build().save()
        ProductFactory.build().save()

    def test_should_create_products_instance(self):

        self.assertEqual(3, len(Product.objects.all()))

    def test_should_return_all_products(self):
        response = self.client.get("/art/products/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["products"]), 3)

    def test_should_return_products_details(self):
        response = self.client.get("/art/products/2/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['product'].id), 2)