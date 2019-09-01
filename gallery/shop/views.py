from django.shortcuts import render


def index(request):
    info = 'shop'
    return render(request, 'shop/index.html', {'info': info})