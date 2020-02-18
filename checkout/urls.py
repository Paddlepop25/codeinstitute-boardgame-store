from django.urls import path

# from .views import checkout, checkout_success, checkout_cancelled
from .views import charge
# , checkout, donate

urlpatterns = [
    # path('donate/', donate, name='donate'),
    # path('charge/', charge, name='charge'),
    path('', charge, name='charge'),
    # path('', checkout, name='checkout'),
    # path('success', checkout_success),
    # path('cancelled', checkout_cancelled)    
]