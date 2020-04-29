from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from .forms import *   # import all forms
from django.contrib.messages import get_messages

# Test forms
class LoginFormTest(TestCase):

    # Valid Form Data
    def test_loginForm_valid(self):
        form = LoginForm(data={'username': 'testing123', 'password': 'user123!'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data - empty username
    def test_loginForm_no_username_invalid(self):
        form = LoginForm(data={'username': '', 'password': 'user123!'})
        self.assertFalse(form.is_valid())
    
    # Invalid Form Data - None username
    def test_loginForm_none_username_invalid(self):
        form = LoginForm(data={'username': None, 'password': 'user123!'})
        self.assertFalse(form.is_valid())

    # Invalid Form Data - empty password
    def test_loginForm_no_password_invalid(self):
        form = LoginForm(data={'username': 'testing123', 'password': ''})
        self.assertFalse(form.is_valid())
    
    # Invalid Form Data - None password
    def test_loginForm_none_password_invalid(self):
        form = LoginForm(data={'username': 'testing123', 'password': None})
        self.assertFalse(form.is_valid())

class RegistrationFormTest(TestCase):

    # Valid Form Data
    def test_registrationform(self):
        valid_data = {
        "username": "testing123",
        "email": "testing123@gmail.com",
        "password1": "user123!",
        "password2": "user123!"
        }
        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
    
    # Invalid Form Data - empty username
    def test_registrationform_empty_username(self):
        invalid_data = {
        "username": "",
        "email": "testing123@gmail.com",
        "password1": "user123!",
        "password2": "user123!"
        }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

    # Invalid Form Data - None email
    def test_registrationform_none_email(self):
        invalid_data = {
        "username": "testing123",
        "email": None,
        "password1": "user123!",
        "password2": "user123!"
        }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

    # Invalid Form Data - Passwords don't match
    def test_registrationform_passwords_dont_match(self):
        invalid_data = {
        "username": "testing123",
        "email": "testing123@gmail.com",
        "password1": "user1234",
        "password2": "user123!"
        }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

# Test views
class Logout_Confirm_Test(TestCase):

    def test_logout_confirm(self):
        url = reverse('logout_confirm')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout_confirm.template.html')
        self.assertContains(response, 'Are you sure you want to logout?')

class Logout_Test(TestCase):

    def test_logout(self):
        url = reverse('logout')
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have successfully logged out.')


class User_Login_View_Test(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='testing123')
        # pw set separated because if included in objects.create, it will be hashed as long string, and cannot be used to compare below
        self.user.set_password('user123!')
        self.user.save()

    def tearDown(self):
        self.user.delete()  

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.template.html')
        self.assertContains(response, 'Login Account')

    def test_after_login_view(self):
        user_login = self.client.login(username='testing123', password='user123!')
        response = self.client.post('/', follow=True)
        self.assertTrue(user_login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.template.html')

class ProfileViewTest(TestCase):

    def test_redirects_to_login_when_notloggedin(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/user/login/?next=/user/profile/")

class User_Registration_View_Test(TestCase):

    def setUp(self):
        self.client = Client()

    def test_registration_view(self):
        url = reverse('register')

        # test request method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.template.html')
        self.assertContains(response, 'Register an Account')

        # test request method POST with valid data
        required_data = {
        "username": "testing123",
        "email": "testing123@gmail.com",
        "password1": "user123!",
        "password2": "user123!"
        }
        response = self.client.post(url, required_data)
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Registration is successful. You can now make payment')

