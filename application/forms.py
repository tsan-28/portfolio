from django import forms
from django.forms import ModelForm
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class profile_updateForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'