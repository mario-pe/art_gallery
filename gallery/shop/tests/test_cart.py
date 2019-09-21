from art.tests.factories import ProductFactory
from django.test import TestCase


class CartTests(TestCase):
    def setUp(self):
        ProductFactory().save()

    def test_if_cart_is_in_session_and_its_not_empty_should_return_products_and_cart_value(
        self
    ):
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session.save()
        response = self.client.get("/shop/cart/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["products"]), 1)

    def test__should_return_response_code_200__if_cart_isnt_in_sesion(self):
        response = self.client.get("/shop/cart/")

        self.assertEqual(response.status_code, 200)

    def test__should_return_form__for_add_number_of_product_when_method_is_get(self):
        response = self.client.get("/shop/add_to_cart/1/")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["form"])

    def test__should_create_cart_add_product_to_cart_and_add_cart_to_session__when_method_is_post_and_form_is_valid(
        self
    ):
        form_data = {"quantity": 2}
        response = self.client.post("/shop/add_to_cart/1/", form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(response.wsgi_request.session.get("cart")), 1)
        self.assertEqual(
            response.wsgi_request.session.get("cart")[0]["product_id"], "1"
        )
        self.assertEqual(response.wsgi_request.session.get("cart")[0]["quantity"], "2")

    def test__should_add_quantity_to_product_in_cart__when_product_exist_in_cart__method_is_post__form_is_valid(
        self
    ):
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session.save()
        form_data = {"quantity": 2}
        response = self.client.post("/shop/add_to_cart/1/", form_data)

        # import ipdb
        # ipdb.set_trace()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(response.wsgi_request.session.get("cart")), 1)
        self.assertEqual(response.wsgi_request.session.get("cart")[0]["product_id"], 1)
        self.assertEqual(response.wsgi_request.session.get("cart")[0]["quantity"], 4)

    def test__should_add_product_to_cart__when_product_not_exist_in_cart__method_is_post__form_is_valid(
        self
    ):
        session = self.client.session
        session["cart"] = [{"product_id": 2, "quantity": 2}]
        session.save()
        form_data = {"quantity": 2}
        response = self.client.post("/shop/add_to_cart/1/", form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(response.wsgi_request.session.get("cart")), 2)
        self.assertEqual(response.wsgi_request.session.get("cart")[0]["product_id"], 2)
        self.assertEqual(response.wsgi_request.session.get("cart")[0]["quantity"], 2)

    def test__should_remove_desired_product_from_cart(self):
        session = self.client.session
        session["cart"] = [{"product_id": 2, "quantity": 2}]
        session.save()

        response = self.client.get("/shop/remove_from_cart/2/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(response.wsgi_request.session.get("cart")), 0)
