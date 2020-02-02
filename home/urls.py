from django.urls import path
from .views import home  # .views is from this same 'home' directory

urlpatterns = [
    path('', home, name="home"),
]