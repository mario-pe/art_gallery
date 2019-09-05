from datetime import datetime

import factory

from art.models import Category, Author, Product


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda a: "Name_{}".format(a + 1))


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Author
        django_get_or_create = ("first_name", "second_name", "birthday", "description")

    first_name = factory.Sequence(lambda a: "First_name_{}".format(a + 1))
    second_name = factory.Sequence(lambda a: "Second_name_{}".format(a + 1))
    birthday = datetime.now()
    description = factory.Sequence(lambda a: "desc_{}".format(a + 1))


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda a: "title_{}".format(a + 1))
    price = factory.Sequence(lambda a: a + 1)
    image = factory.django.ImageField(filename="the_image.dat")
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for author in extracted:
                self.authors.add(author)
