from django.shortcuts import render, get_object_or_404

from art.models import Author


def authors(request):
    authors = Author.objects.all()
    return render(request, 'art/authors/authors.html', {'authors': authors})

def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'art/authors/author_details.html', {'author': author})
