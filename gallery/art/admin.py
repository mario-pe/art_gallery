from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "birthday", "description")


class ProductAdmin(admin.ModelAdmin):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    list_display = ("title",)
