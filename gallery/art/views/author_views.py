from django.shortcuts import render, get_object_or_404

from art.models import Author

from art.models import Product


def authors(request):
    authors = Author.objects.all()
    return render(request, "art/authors/authors.html", {"authors": authors})


def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author_products = Product.objects.filter(authors=author_id).all()
    return render(
        request,
        "art/authors/author_details.html",
        {"author": author, "author_products": author_products},
    )
