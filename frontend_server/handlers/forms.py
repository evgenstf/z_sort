from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder':'Your login'}
        )
    )
    email = forms.CharField(
        widget = forms.EmailInput(
            attrs = {'placeholder':'Your email'}
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {'placeholder':'Come up with a good password'}
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {'placeholder':'And type it in once more'}
        )
    )

