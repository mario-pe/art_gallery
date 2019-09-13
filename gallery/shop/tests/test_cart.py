# from django.test import TestCase
#
# from shop.models import Cart
# # from art.models import Product
#
# from shop.tests.factories import CartFactory
# # from art.tests.factories import ProductFactory
#
#
# class CartTests(TestCase):
#     def setUp(self) -> None:
#         CartFactory.build().save()
#         # ProductFactory().save()
#         # ProductFactory().save()
#         # ProductFactory().save()
#
#     def test_should_create_cart_instance(self):
#         assert 1 == 2
#         # self.assertEqual(1, len(Cart.objects.all()))
#
#     def test_should_add_product_to_cart(self):
#         response = self.client.get("/shop/add_to_cart/1/")
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context["cart"]), 1)
#
#     def test_should_return_cart_without_product_if_porduct_is_removed(self):
#         pass
#
#     def test_should_return_empty_cart_after_when_order_is_made(self):
#         pass
