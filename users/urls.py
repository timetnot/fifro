from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("confirm-code/", views.confirm_code_view, name="confirm_code"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # Или ваша форма

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Замените на вашу форму регистрации
        if form.is_valid():
            user = form.save()
            return redirect('profile')  # Редирект на профиль после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
