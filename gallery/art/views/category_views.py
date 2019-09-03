from django.shortcuts import render, get_object_or_404
from art.models import Category

def categories(request):
    categories = Category.objects.all()
    return render(request, 'art/authors/authors.html', {'categories': categories})