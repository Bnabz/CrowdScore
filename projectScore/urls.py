"""projectScore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse_lazy
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', include('appScore.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/',RegistrationView.as_view(success_url=reverse_lazy('my_profile')),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('api_token-auth/',obtain_auth_token),
]

