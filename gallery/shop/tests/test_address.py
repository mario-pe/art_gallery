from art.tests.factories import ProductFactory
from django.test import TestCase
from account.models import User
from shop.models import Client


class AddressTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="c1",
            first_name="name_c1",
            last_name="sure_name_c1",
            password="123456Mp",
            email="c1@c1.c1",
        )
        self.shop_client = Client.objects.create(user=self.user)
        ProductFactory().save()

    def test__should_return_add_address_form_if_method_is_get(self):
        response = self.client.get("/shop/add_address/")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["form"])

    def test_should_add_address_to_desired_clinet_if_form_is_valid(self):
        self.client.force_login(user=self.user)
        session = self.client.session
        session["cart"] = [{"product_id": 1, "quantity": 2}]
        session.save()
        address_data = {
            "city": "city_4",
            "street": "street_4",
            "number": "44",
            "zip_code": "44-111",
        }

        response = self.client.post("/shop/add_address/", address_data)

        self.assertEqual(response.status_code, 200)
