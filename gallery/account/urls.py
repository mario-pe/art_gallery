from django.conf.urls import url
from account.views import UserSignUpView


app_name = "account"

urlpatterns = [
    url(r"^user_signup/$", UserSignUpView.as_view(), name="user_signup")
]
