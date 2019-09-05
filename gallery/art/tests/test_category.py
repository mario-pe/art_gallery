from art.models import Category
from art.tests.factories import CategoryFactory, ProductFactory
from django.test import TestCase


class AuthorTests(TestCase):
    def setUp(self) -> None:
        CategoryFactory.build().save()
        CategoryFactory.build().save()
        CategoryFactory.build().save()

    def test_should_create_category_instance(self):

        self.assertEqual(3, len(Category.objects.all()))

    def test_should_return_all_categories(self):
        response = self.client.get("/art/categories/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["categories"]), 3)

    def test_should_return_all_products_related_with_category(self):
        category = Category.objects.first()
        ProductFactory(category=category).save()
        ProductFactory(category=category).save()

        response = self.client.get("/art/category/1/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category"].id, category.id)
        self.assertEqual(len(response.context["category"].product_set.all()), 2)
