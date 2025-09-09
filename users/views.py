from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm, LoginForm
import random

confirmation_codes = {}

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = False
            user.save()

            code = str(random.randint(100000, 999999))
            confirmation_codes[user.email] = code

            send_mail(
                "Код подтверждения Vivro",
                f"код подтверждения: {code}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            request.session["registration_email"] = user.email
            messages.success(request, "Код подтверждения выслан на вашу почту.")
            return redirect("users:confirm_code")
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

def confirm_code_view(request):
    if request.method == "POST":
        code_entered = request.POST.get("code")
        email = request.session.get("registration_email")

        if email and code_entered and confirmation_codes.get(email) == code_entered:
            users = User.objects.filter(email=email)
            if users.exists():
                user = users.first()
                user.is_active = True
                user.save()
                confirmation_codes.pop(email, None)
                request.session.pop("registration_email", None)
                messages.success(request, "регистрация подтверждена. теперь вы можете войти.")
                return redirect("users:login")
            else:
                messages.error(request, "пользователь не найден.")
        else:
            messages.error(request, "неверный код подтверждения.")
    return render(request, "users/confirm_code.html")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"добро пожаловать, {user.username}!")
            return redirect("index") 
        else:
            messages.error(request, "неверное имя пользователя или пароль.")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "вы вышли из системы.")
    return redirect("index")
