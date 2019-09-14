from .models import *
from django import forms


class OrderProductForm(forms.Form):
    quantity = forms.IntegerField(label='Ilość', min_value=1)


class NoLoggedUserOrder(forms.Form):
    first_name = forms.CharField(label="Imie", max_length=100)
    second_name = forms.CharField(label="Nazwisko", max_length=100)

    email = forms.EmailField(label="Email", max_length=100)

    street = forms.CharField(label="Ulica", max_length=100)
    number = forms.CharField(label="Numer budynku", max_length=100)
    zip_code = forms.CharField(label="Kod pocztowy", max_length=100)
    city = forms.CharField(label="Miasto", max_length=100)
