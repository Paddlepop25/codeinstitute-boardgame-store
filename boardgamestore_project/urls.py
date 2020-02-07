"""boardgamestore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from accounts.views import index as accounts_index, logout, login, profile, register

# when user go to user/profile url, it sill call the register function, and we'll call this route register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('user/', include('accounts.urls')),
    path('user/', include('django.contrib.auth.urls')),
    # path('user/', accounts_index, name='user_index'),
    # path('user/logout', logout, name='logout'),
    # path('user/login', login, name='login'),
    # path('user/profile', profile, name='profile'),
    # path('user/register', register, name='register'),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('info_pages/', include('info_pages.urls')),
]
