import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import DateField
from django.utils.translation import ugettext_lazy as _

from shop.models import Client

User = get_user_model()


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name')
        model = User
        labels = {
            'username': 'Login',
            'first_name': 'Imie',
            'last_name': 'Nazwisko',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        if commit:
            user.save()
        point_of_care = self.cleaned_data.get('point_of_care')
        Client.objects.create(user=user, point_of_care=point_of_care)
        return user

    error_messages = {
            'unique': "Uzytkownik o takim loginie istnieje.",
            'password_mismatch': "Hasła muszą być identyczne.",
    }