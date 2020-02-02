from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 
    
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']    
        
    def clean_email(self):
        user_email = self.cleaned_data.get('email') # email from form
        username = self.cleaned_data.get('username') # username from form
        
        User = get_user_model()
        
        # checking is email has been used by a user before
        # comparable to SELECT * FROM User WHERE email='{}'.format(user_email)
        if User.objects.filter(email=user_email):
            raise forms.ValidationError('This email address has already been used')
            
        return user_email # django requirement, email user typed in form will be returned if not been used before 
        
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Password does not match")
    
        return password1