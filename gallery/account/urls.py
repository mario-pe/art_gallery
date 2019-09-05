from django.conf.urls import url
from account.views import UserSignUpView

# from django.contrib.auth.views import login, logout

app_name = "account"

urlpatterns = [
    # url(r'^login/$', login, name='login'),
    # url(r'^logout/$', logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r"^user_signup/$", UserSignUpView.as_view(), name="user_signup")
]
