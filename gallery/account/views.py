from django.shortcuts import render, redirect

from account.models import User
from account.forms import UserSignUpForm
from django.contrib.auth import login
from django.views.generic import CreateView


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("art:products")
