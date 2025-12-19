from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
