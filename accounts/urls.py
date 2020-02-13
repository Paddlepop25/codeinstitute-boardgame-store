from django.urls import path, include
from .views import index, logout, logout_confirm, login, profile, register, my_account, password_reset
from home.views import home

urlpatterns = [
    # path('', index, name='user_index'),
    # path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('logout_confirm/', logout_confirm, name='logout_confirm'),
    path('password_reset/', password_reset, name='password_reset'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('my_account/', my_account, name='my_account'),
    
]