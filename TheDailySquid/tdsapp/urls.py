from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from tdsapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile.html', profile, name='user profile'),

    path('signup.html', signup, name='signup'),
    path('login.html', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout.html', auth_views.LogoutView.as_view(), name='logout'),
]
