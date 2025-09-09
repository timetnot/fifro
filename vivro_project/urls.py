from django.urls import path
from mainapp import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('health/', views.health, name='health'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('career/', views.career, name='career'),
    path('life/', views.life, name='life'),
    path('family/', views.family, name='family'),
    path('sports/', views.sports, name='sports'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('profile/', views.profile_view, name='profile'),
]