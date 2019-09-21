from art.tests.factories import ProductFactory
from django.test import TestCase
from account.models import User
from shop.models import Client, Address, Order, OrderProduct
from art.models import Product


class OrderTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="c1",
            first_name="name_c1",
            last_name="sure_name_c1",
            password="123456Mp",
            email="c1@c1.c1",
        )
        self.shop_client = Client.objects.create(user=self.user)
        ProductFactory().save()
        self.address = Address.objects.create(
            street="street_c1",
            number="c1_2",
            zip_code="15-100",
            city="c1_city",
            client=self.shop_client,
        )



    def test_should_redirect_to__prepare_logged_order__if_user_is_logged(self):
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session.save()

        self.client.force_login(user=self.user)
        response = self.client.get("/shop/confirm_order/")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["client"])
        self.assertIsNotNone(response.context["addresses"])
        self.assertIsNotNone(response.context["personal_data"])
        self.assertIsNotNone(response.context["cart"])
        self.assertIsNotNone(response.context["products"])
        self.assertIsNotNone(response.context["cart_value"])

    def test_should_return_client_form__if_user_is_not_logged(self):
        response = self.client.get("/shop/confirm_order/")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context.get("form"))

    def test_should_return_personal_data_and_cart__of_not_logged_clinet(self):
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session.save()
        personal_data = {
            "first_name": "fn_c1",
            "last_name": "ln_c1",
            "email": "c1@c1.pl",
            "street": "street_c1",
            "number": "c1_2",
            "zip_code": "15-100",
            "city": "c1_city",
        }
        response = self.client.post("/shop/confirm_order/", personal_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["personal_data"])
        self.assertEqual(len(response.context["cart"]), 1)
        self.assertEqual(len(response.context["products"]), 1)
        self.assertIsNotNone(response.context["cart_value"])

    def test_should_create_oder_instnace_from_cart__for_logged_user(self):
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session.save()
        self.client.force_login(user=self.user)
        response = self.client.post("/shop/make_logged_user_order/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Order.objects.all()), 1)


    def test_should_create_oder_instnace_from_cart__for_not_logged_user(self):
        personal_data = {
            "first_name": "fn_c1",
            "last_name": "ln_c1",
            "email": "c1@c1.pl",
            "street": "street_c1",
            "number": "c1_2",
            "zip_code": "15-100",
            "city": "c1_city",
        }
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session["personal_data"] = personal_data
        session.save()
        response = self.client.post("/shop/make_no_logged_user_order/")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["products"])

    def test_should_return__user_order_hisory(self):
        self.client.force_login(user=self.user)

        response = self.client.get("/shop/user_order_history/")

        self.assertEqual(response.status_code, 200)

    def test_should_return__order_details(self):
        self.__prepare_order()

        response = self.client.get("/shop/order_details/1/")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["order_products"])

    def __prepare_order(self):
        product = Product.objects.all()[0]
        product.value = 2.0
        op = OrderProduct.objects.create(product=product, quantity=2, value=4.0)
        Order.objects.create(address=self.address, client=self.shop_client)
        # pass
