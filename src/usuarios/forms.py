from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name')