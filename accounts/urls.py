from django.urls import path, include
from .views import logout, logout_confirm, login, profile, register
# from home.views import home

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('logout_confirm/', logout_confirm, name='logout_confirm'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    
]