from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'accounts/index.template.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out") # flash message
    return redirect( reverse('user_index'))

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] # username from form
        password = request.POST['password'] # password from form

        # check if username and password matches
        user = auth.authenticate(username=username, password=password)

        # Recreate form with the user's input submitted via POST
        login_form = LoginForm(request.POST)

        # if a user is valid and returned by auth.authenticate
        if user:
            # log the user in
            auth.login(user=user, request=request)
            messages.success(request, 'You have logged in successfully') # flash message
            return redirect(reverse('user_index'))
        else:
            # if user is None, show flash message
            login_form.add_error(None, "Invalid user name or password")
            return render(request, 'accounts/login.template.html', {
            'login_form':login_form
        })
    else:
        login_form = LoginForm()
        return render(request, 'accounts/login.template.html', {
            'login_form':login_form
        }) 
