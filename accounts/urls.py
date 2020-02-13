from django.urls import path, include
from .views import index, logout, logout_confirm, login, profile, register, my_account, password_reset, password_reset_done
from home.views import home

urlpatterns = [
    # path('', index, name='user_index'),
    # path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('logout_confirm/', logout_confirm, name='logout_confirm'),
    path('password_change/', password_reset, name='password_change'),  
    path('password_change_done/', password_reset_done, name='password_change_done'),  
    path('password_reset/', password_reset, name='password_reset'),  
    path('password_reset_done/', password_reset_done, name='password_reset_done'),  
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('my_account/', my_account, name='my_account'),
    
]