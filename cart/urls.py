from django.urls import path

from .views import add_to_cart, view_cart, remove_from_cart, checkout_form

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<game_id>', add_to_cart, name='add_to_cart'),
    path('remove/<game_id>', remove_from_cart, name='remove_from_cart'),
    path('checkout_form/', checkout_form, name='checkout_form'),
]