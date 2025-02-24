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

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(max_length=100, label='Subject')
    description = forms.CharField(widget=forms.Textarea, required=False, label='Description')
    attachment = forms.FileField(label='Attachment')