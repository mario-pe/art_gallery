from .models import *
from django import forms


class OrderProductForm(forms.Form):
    quantity = forms.IntegerField(label='Ilość', min_value=1)