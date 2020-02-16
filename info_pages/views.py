from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('info_pages/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, "Thank you for your query. We will contact you shortly.")
            return redirect('contact_us')
            
    return render(request, "info_pages/contact_us.template.html", {
        'form':form_class
    })
    
def terms_and_conditions(request):
    return render(request, "info_pages/terms_and_conditions.template.html")
    
def privacy_policy(request):
    return render(request, "info_pages/privacy_policy.template.html")

def refund_policy(request):
    return render(request, "info_pages/refund_policy.template.html")
