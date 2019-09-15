from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name")
        model = User
        labels = {"username": "Login", "first_name": "Imie", "last_name": "Nazwisko"}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        if commit:
            user.save()
        return user

    error_messages = {
        "unique": "Uzytkownik o takim loginie istnieje.",
        "password_mismatch": "Hasła muszą być identyczne.",
    }
