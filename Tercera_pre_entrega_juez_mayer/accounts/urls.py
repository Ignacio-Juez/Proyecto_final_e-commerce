from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import register, login_request, custom_logout, edit_profile
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]