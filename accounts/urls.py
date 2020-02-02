from django.urls import path, include
from .views import index, logout, login, profile, register, my_account

urlpatterns = [
    path('', index, name='user_index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('my_account/', my_account, name='my_account'),
    
]