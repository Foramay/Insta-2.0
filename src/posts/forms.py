from django import forms
from .models import Posts
from django.forms import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['descripcion']