from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        User = get_user_model()
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
