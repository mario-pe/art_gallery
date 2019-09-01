from art.models import Author
from art.tests.factories import AuthorFactory, ProductFactory
from django.test import TestCase


class AuthorTests(TestCase):
    def setUp(self) -> None:
        AuthorFactory.build().save()
        AuthorFactory.build().save()
        AuthorFactory.build().save()

    def test_should_create_author_instance(self):

        self.assertEqual(3, len(Author.objects.all()))

    def test_should_return_all_authors(self):
        response = self.client.get("/art/authors/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["authors"]), 3)

    def test_should_return_desired_author_details_with_list_of_related_products(self):
        product1 = ProductFactory().build(author=1)
        product2 = ProductFactory().build(author=1)
        response = self.client.get("/art/authors/2/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["author"].id, 2)
        self.assertEqual(len(response.context['products']), 2)