from django.shortcuts import render


def index(request):
    info = 'art'
    return render(request, 'index.html', {'info': info})