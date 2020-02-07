from django.shortcuts import render

# Create your views here.
def terms_and_conditions(request):
    return render(request, "info_pages/terms_and_conditions.template.html")
    
def privacy_policy(request):
    return render(request, "info_pages/privacy_policy.template.html")

def refund_policy(request):
    return render(request, "refund_policy.template.html")