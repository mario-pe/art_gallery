from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.name)


class Author(models.Model):
    first_name = models.CharField(max_length=256)
    second_name = models.CharField(max_length=256)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)


class Product(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def get_authors(self):
        return ",".join([str(p) for p in self.authors.all()])

    def __str__(self):
        return "{}, {}".format(self.title, self.category)
