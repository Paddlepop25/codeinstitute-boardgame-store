from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from .models import MyUser

# Create your views here.
def index(request):
    return render(request, 'accounts/index.template.html')

def logout_confirm(request):
    return render(request, 'accounts/logout_confirm.template.html')

# def password_reset(request):
#     return render(request, 'accounts/password_reset.template.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out.") # flash message
    # return redirect( reverse('user_index'))
    return redirect( reverse('home'))

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
            messages.success(request, 'Successfully signed in as ' + username) # flash message
            # return redirect(reverse('user_index'))
            return redirect( reverse('home'))
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
    
@login_required        
def profile(request):
    User = MyUser
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.template.html', {
        'user' : user
    })
    
def register(request):
    # when user submit form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): # django check through fields one by one to validate. check email will run clean email
            form.save() # registration is successful, form will be saved
        
        # log in user
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
        
        if user:
            auth.login(user=user, request=request)
            messages.success(request, "Registration is successful. You can checkout")
            return redirect(reverse('user_index'))
        else:    
            messages.error(request, "Sorry, we're unable to register your account.")
            print(messages.error)
            return redirect(reverse('home'))
            
    else:
        # if registration fail
        register_form = RegistrationForm()
        return render(request, 'accounts/register.template.html', {
            'form': register_form
    })    
    
def my_account(request):
    return render(request, 'accounts/my_account.template.html')    