from django.urls import path
from .views import terms_and_conditions, privacy_policy, refund_policy

urlpatterns = [
    path('terms_and_conditions/', terms_and_conditions, name="terms_and_conditions"),
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('refund_policy/', refund_policy, name="refund_policy")
]