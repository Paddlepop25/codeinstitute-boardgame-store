from django.urls import path
from .views import contact_us, terms_and_conditions, privacy_policy, refund_policy

urlpatterns = [
    path('contact_us/', contact_us, name="contact_us"),
    path('terms_and_conditions/', terms_and_conditions, name="terms_and_conditions"),
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('refund_policy/', refund_policy, name="refund_policy")
]