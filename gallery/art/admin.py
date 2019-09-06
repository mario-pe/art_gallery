from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "birthday", "description")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "image", "category", "get_authors")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Product, ProductAdmin)