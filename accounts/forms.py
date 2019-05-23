from django import forms
from django.forms.widgets import PasswordInput, EmailInput
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20, min_length=3, required=True)
    password = forms.CharField(label='password', max_length=30, min_length=8, widget=PasswordInput, required=True)


class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=20, min_length=3, required=True)
    first_name = forms.CharField(label='first_name', max_length=20, min_length=3, required=True)
    last_name = forms.CharField(label='last_name', max_length=20)
    password = forms.CharField(label='password', widget=PasswordInput, min_length=8, max_length=30, required=True)
    password2 = forms.CharField(label='password2', widget=PasswordInput, min_length=8, max_length=30, required=True)
    email = forms.CharField(label='email', widget=EmailInput, required=True)
    mobile = forms.RegexField("[0-9]{10}", label='mobile', max_length=10, min_length=10)

    def is_valid(self):
        if super().is_valid():
            values = self.cleaned_data
            if get_user_model().objects.filter(username=values['username']).count() != 0:
                return False
            elif values['password'] != values['password2']:
                return False
            else:
                return True
