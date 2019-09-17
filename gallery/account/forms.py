from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from shop.models import Client

User = get_user_model()


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")
        model = User
        labels = {"username": "Login", "first_name": "Imie", "last_name": "Nazwisko"}

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            client = Client(user=user)
            client.save()
        return user

    error_messages = {
        "unique": "Uzytkownik o takim loginie istnieje.",
        "password_mismatch": "Hasła muszą być identyczne.",
    }
