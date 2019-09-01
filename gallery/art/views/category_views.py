from django.shortcuts import render


def index(request):
    info = 'art'
    return render(request, 'art/index.html', {'info': info})