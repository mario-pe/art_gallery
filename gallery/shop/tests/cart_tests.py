from django.test import TestCase

from shop.models import Cart

from shop.ttests.factories import CartFactory


class CartTests(TestCase):
    def setUp(self) -> None:
        CartFactory.build().save()
        CartFactory.build().save()
        CartFactory.build().save()

    def test_should_create_cart_instance(self):

        self.assertEqual(3, len(Cart.objects.all()))

    def test_should_add_product_to_cart(self):
        pass

    def test_should_return_cart_without_product_if_porduct_is_removed(self):
        pass

    def test_should_return_empty_cart_after_when_order_is_made(self):
        pass
