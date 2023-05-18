import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    password_validation
)

from .models import User
from transactions.models import Balance


def home(request):
    a = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').json()[0]['buy']

    return render(request, 'home.html', context={'home_page': True, 'usd_price': a})


def sing_in(request):
    if request.user.is_authenticated:
        return redirect("users:home")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in as " + email)
            return redirect("users:home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request=request, template_name="accounts/login.html", context={"login_page": True})


def sing_up(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already in use.")
            return redirect("users:register")

        try:
            password_validation.validate_password(password)
        except ValidationError as error_messages:
            messages.error(request, error_messages.messages[0])
            return redirect("users:register")

        user = User.objects.create_user(
            email=email,
            password=password
        )

        balance = Balance(
            user=user
        )
        balance.save()


        login(request, user)

        messages.success(request, "Welcome, home :)")

        return redirect("users:home")

    return render(request, "accounts/register.html", context={"login_page": True})


@login_required
def sign_out(request):
    logout(request)
    return redirect("users:home")
