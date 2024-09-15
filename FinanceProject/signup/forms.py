from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserData

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'name', 'email', 'phone_number', 'age', 'risk', 'income', 'disposable_income', 'goal1', 'goal2', 'goal3']


