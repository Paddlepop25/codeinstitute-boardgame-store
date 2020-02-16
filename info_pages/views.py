from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    form = ContactForm
    return render(request, "info_pages/contact_us.template.html", {
        'form':form
    })
    
def terms_and_conditions(request):
    return render(request, "info_pages/terms_and_conditions.template.html")
    
def privacy_policy(request):
    return render(request, "info_pages/privacy_policy.template.html")

def refund_policy(request):
    return render(request, "info_pages/refund_policy.template.html")
